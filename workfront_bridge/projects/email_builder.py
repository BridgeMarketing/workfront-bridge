import sys

from workfront.objects.template_project import WFTemplateProject

from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.projects.email import WFProjectEmailContainer
from workfront_bridge.blocks.email import WFEmailTestSeedNoEmailSentBlock, \
    WFEmailAudienceLiveSetupBlock, WFEmailReviewDeploymentBlock
from workfront_bridge.blocks.email import WFEmailLiveSeedBlock
from workfront_bridge.blocks.email import WFEmailTestSeedBlock
from workfront_bridge.blocks.email import WFEmailGenHtmlFromZipBlock
from workfront_bridge.blocks.email import WFEmailValidateHtmlBlock
from datetime import datetime


class ProviderConfig(object):
    def __init__(self):
        self.name = None
        self.user = None
        self.password = None
        self.token = None
        self.sender_email = None
        self.sender_name = None


class EmailProjectBuilder(object):
    '''
    @summary: Email project builder to easily construct email workfront
    projects.
    '''

    def __init__(self, wf, project_name):
        '''
        @param wf: Workfront service object
        @param project_name: that the created will have.
        '''
        self.project_name = project_name
        self.wf = wf
        self.live_seed_list = None
        self.test_seed_lists = []
        self.subject = None
        self.html = None
        self.html_zip = None
        self.provider = None
        self.test_sl_send_emails = True
        self.review_deployment = True

        self.audience_provider = ProviderConfig()
        self.seeds_provider = ProviderConfig()

    def set_html(self, s3_path):
        self.html = s3_path
        return self

    def set_html_zip(self, s3_path):
        self.html_zip = s3_path
        return self

    def add_test_list(self, s3_path):
        self.test_seed_lists.append(s3_path)
        return self

    def set_seed_list(self, s3_path):
        self.live_seed_list = s3_path
        return self

    def set_send_validate_test_seed_emails(self, val=True):
        self.test_sl_send_emails = val
        return self

    def set_subject(self, subject):
        self.subject = subject
        return self

    def set_review_deployment(self, val=True):
        self.review_deployment = val
        return self

    def set_deployment_datetime(self, dt):
        self.deployment_time = dt
        return self

    def set_audience_sender_email(self, email):
        self.audience_provider.sender_email = email
        return self

    def set_audience_sender_name(self, name):
        self.audience_provider.sender_name = name
        return self

    def set_audience_provider(self, esp_name, esp_user=None, password=None,
                              token=None):
        self.audience_provider.name = esp_name
        self.audience_provider.user = esp_user
        self.audience_provider.password = password
        self.audience_provider.token = token
        return self

    def set_seeds_sender_email(self, email):
        self.seeds_provider.sender_email = email
        return self

    def set_seeds_sender_name(self, name):
        self.seeds_provider.sender_name = name
        return self

    def set_seeds_provider(self, esp_name, esp_user=None, password=None,
                           token=None):
        self.seeds_provider.name = esp_name
        self.seeds_provider.user = esp_user
        self.seeds_provider.password = password
        self.seeds_provider.token = token
        return self

    def _configure_provider_in_setup_block(self, block, provider):
        block.sender_email = provider.sender_email
        block.sender_name = provider.sender_name

        block.provider = provider.name
        block.provider_user = provider.user
        block.provider_password = provider.password
        block.provider_token = provider.token

    def _crt_audience_block(self):
        audb = WFEmailAudienceLiveSetupBlock()
        audb.campaign_name = self.project_name
        audb.deployment_datetime = self.deployment_time
        audb.seed_list_s3_path = self.live_seed_list
        self._configure_provider_in_setup_block(audb, self.audience_provider)
        return audb

    def _crt_test_list_block(self, test_list):
        slb = None
        if self.test_sl_send_emails:
            slb = WFEmailTestSeedBlock()
            slb.seed_list_s3_path = test_list
            slb.campaign_name = "Test List - " + self.project_name
            slb.deployment_datetime = datetime.now()
            self._configure_provider_in_setup_block(slb, self.seeds_provider)
        else:
            slb = WFEmailTestSeedNoEmailSentBlock()
            slb.seed_list_s3_path = test_list
        return slb

    def _check_viability(self):
        if self.html is None and self.html_zip is None:
            err = "At least a zip or an html should be provided"
            raise WFBrigeException(err)

        if self.html is not None and self.html_zip is not None:
            err = "Only a zip or an html should be provided"
            raise WFBrigeException(err)

        def check_not_none(name, value):
            if value is None:
                raise WFBrigeException("{} is required".format(name))

        check_not_none("subject", self.subject)

        check_not_none("audience_provider", self.audience_provider.name)
        check_not_none("audience_sender_name",
                       self.audience_provider.sender_name)
        check_not_none("audience_sender_email",
                       self.audience_provider.sender_email)

        if len(self.test_seed_lists) > 0:
            check_not_none("seeds_provider", self.seeds_provider.name)
            check_not_none("seeds_sender_name",
                           self.seeds_provider.sender_name)
            check_not_none("seeds_sender_email",
                           self.seeds_provider.sender_email)

    def build(self):
        '''
        @summary: According to all the parameters set to the builder, build a
        workfront project.
        @raise WFBrigeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        '''
        self._check_viability()

        project = WFProjectEmailContainer(self.project_name)
        project.email_subject = self.subject

        if self.html_zip is not None:
            zipb = WFEmailGenHtmlFromZipBlock()
            zipb.zip_s3_path = self.html_zip
            project.append(zipb)
        else:
            project.html_s3_path = self.html

        bval_html = WFEmailValidateHtmlBlock()
        bval_html.email_subject = self.subject
        project.append(bval_html)

        for test_list in self.test_seed_lists:
            slb = self._crt_test_list_block(test_list)
            project.append(slb)

        if self.live_seed_list is not None:
            email_seed_block = WFEmailLiveSeedBlock()
            email_seed_block.seed_list_s3_path = self.live_seed_list
            project.append(email_seed_block)

        audb = self._crt_audience_block()
        project.append(audb)

        if self.review_deployment:
            reviewb = WFEmailReviewDeploymentBlock()
            project.append(reviewb)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        return wf_project


class EmailOnBoardingProjectBuilder(object):
    '''
    @summary: Email project onboarding builder to easily construct email workfront
    projects.
    '''

    def __init__(self, wf, project_name):
        '''
        @param wf: Workfront service object
        @param project_name: that the created will have.
        '''
        self.project_name = project_name
        self.wf = wf
        self.live_seed_list = None
        self.test_seed_lists = []
        self.subject = None
        self.html = None
        self.category = None
        self.from_line = None
        self.suppression_file_path = None
        self.client_id = None

        self.__project = None

    def set_html(self, s3_path):
        self.html = s3_path
        return self

    def add_test_list(self, s3_path):
        self.test_seed_lists.append(s3_path)
        return self

    def set_live_seed_list(self, s3_path):
        self.live_seed_list = s3_path
        return self

    def set_subject(self, subject):
        self.subject = subject
        return self

    def set_category(self, category):
        self.category = category

    def set_from_line(self, from_line):
        self.from_line = from_line

    def set_suppression_file_path(self, s3_path):
        self.suppression_file_path = s3_path

    def set_client_id(self, client_id):
        self.client_id = client_id

    def _check_viability(self):

        def check_not_none(name, value):
            if value is None:
                raise WFBrigeException("{} is required".format(name))

        def check_file_extension(name, file_name, allowed_extensions=(".html",)):
            if not file_name.lower().endswith(allowed_extensions):
                raise WFBrigeException(
                    "{}: {} file hasn't an allowed extensions ({})".format(name, file_name,
                                                                           ",".join(allowed_extensions)))

        def check_files_extension(name, files_name=[], allowed_extensions=None):
            for file_name in files_name:
                check_file_extension(name, file_name, allowed_extensions)

        def check_length(field_name, collection, min_length=0, max_length=sys.maxint):
            if len(collection) < min_length or len(collection) > max_length:
                raise WFBrigeException(
                    "{}: length ({}) is not between {} to {}".format(field_name, len(collection), min_length,
                                                                     max_length))

        check_not_none("subject", self.subject)
        check_not_none("html", self.html)
        check_file_extension("html", self.html, (".html", ".zip"))
        check_not_none("category", self.category)
        check_not_none("from_line", self.from_line)
        check_file_extension("live_seed_list", self.live_seed_list, (".csv",))

        check_length("test_seed_lists", self.test_seed_lists, 1, 5)
        check_files_extension("test_seed_lists", self.test_seed_lists, (".csv",))

        if self.suppression_file_path is not None:
            check_file_extension("suppression_file_path", self.suppression_file_path, (".csv",))

        check_not_none("client_id", self.client_id)

    def _get_parameter_test_send_email(self):
        template = WFTemplateProject.from_name(self.wf, self.__project.wf_template_name)
        parameters = template.get_param_values()
        return parameters["test_send_email"]

    def _get_parameter_selected_provider(self):
        template = WFTemplateProject.from_name(self.wf, self.__project.wf_template_name)
        parameters = template.get_param_values()
        return parameters["SelectedProvider"]

    def _create_test_list_block(self, test_list, prefix, sender_email, selected_provider):
        slb = WFEmailTestSeedBlock()
        slb.seed_list_s3_path = test_list
        slb.campaign_name = "T" + prefix + "_" + self.project_name
        slb.deployment_datetime = datetime.now()
        slb.sender_email = sender_email
        slb.sender_name = self.from_line
        slb.provider = selected_provider
        return slb

    def build(self):
        '''
        @summary: According to all the parameters set to the builder, build a
        workfront project.
        @raise WFBrigeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        '''
        self._check_viability()

        parser = WFBlockParser(self.wf)

        self.__project = WFProjectEmailContainer(self.project_name)
        project = self.__project

        project.email_subject = self.subject
        project.from_line = self.from_line
        project.suppression_file_path = self.suppression_file_path
        project.client_id = self.client_id
        project.category = self.category

        if self.html.lower().endswith(".zip"):
            zipb = WFEmailGenHtmlFromZipBlock()
            zipb.zip_s3_path = self.html
            project.append(zipb)
        else:
            project.html_s3_path = self.html

        bval_html = WFEmailValidateHtmlBlock()
        bval_html.email_subject = self.subject
        project.append(bval_html)

        test_send_email = self._get_parameter_test_send_email()
        selected_provider = self._get_parameter_selected_provider()

        for index, test_list in enumerate(self.test_seed_lists, start=1):
            slb = self._create_test_list_block(test_list, str(index), test_send_email, selected_provider)
            project.append(slb)

        project.test_seed_lists = ",".join(self.test_seed_lists)

        email_live_seed_block = WFEmailLiveSeedBlock()
        email_live_seed_block.seed_list_s3_path = self.live_seed_list

        project.live_seed_list = self.live_seed_list

        project.append(email_live_seed_block)

        wf_project = parser.create(project)

        wf_project.set_fields({"portfolioID": self.client_id})

        return wf_project
