from dateutil import tz
from workfront.objects.template_project import WFTemplateProject

from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.projects.email import WFProjectEmailContainer
from workfront_bridge.blocks.email import WFEmailAudienceLiveSetupBlock, \
    WFEmailReviewDeploymentBlock, WFEmailApproveCWTaggingBlock, WFEmailPushToDWHAndEL
from workfront_bridge.blocks.email import WFEmailLiveSeedBlock
from workfront_bridge.blocks.email import WFEmailLiveSeedValidateBlock, \
    WFEmailLiveSeedSendBlock
from workfront_bridge.blocks.email import WFEmailGenHtmlFromZipBlock
from workfront_bridge.blocks.email import WFEmailValidateHtmlBlock


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
        self.subject = None
        self.subject_test_prefix = None
        self.html = None
        self.html_zip = None
        self.provider = None
        self.test_sl_send_emails = True
        self.review_deployment = True
        self.email_creative_id = None
        self.ttd_advertiser_id = None 
        self.ttd_bonus_media_advertiser_id = None 
        self.lr_account_id = None 
        self.lr_bonus_media_account_id = None

        self.audience_provider = ProviderConfig()
        self.seeds_provider = ProviderConfig()
        self.live_seeds_provider = ProviderConfig()

        self.is_created_from_onboarding = False
        self.ecm_html = None
        self.add_tags_weight_approval_step = False
        self.deployment_time = None
        self.project_id = None

    def set_project_id(self, project_id):
        self.project_id = project_id
        return self

    def set_html(self, s3_path):
        self.html = s3_path
        return self

    def set_html_zip(self, s3_path):
        self.html_zip = s3_path
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

    def set_subject_test_prefix(self, subject_test_prefix):
        self.subject_test_prefix = subject_test_prefix
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

    def set_live_seeds_sender_email(self, email):
        self.live_seeds_provider.sender_email = email
        return self

    def set_live_seeds_sender_name(self, name):
        self.live_seeds_provider.sender_name = name
        return self

    def set_live_seeds_provider(self, esp_name, esp_user=None, password=None, token=None):
        self.live_seeds_provider.name = esp_name
        self.live_seeds_provider.user = esp_user
        self.live_seeds_provider.password = password
        self.live_seeds_provider.token = token
        return self

    def set_email_creative_id(self, id):
        self.email_creative_id = id
        return self

    def set_ttd_advertiser_id(self, id):
        self.ttd_advertiser_id = id
        return self

    def set_ttd_bonus_media_advertiser_id(self, id):
        self.ttd_bonus_media_advertiser_id = id
        return self
    
    def set_lr_account_id(self, id):
        self.lr_account_id = id
        return self

    def set_lr_bonus_media_account_id(self,id):
        self.lr_bonus_media_account_id = id
        return self

    def set_is_created_from_onboarding(self, is_from_onboarding):
        self.is_created_from_onboarding = is_from_onboarding
        return self

    def set_ecm_html(self, s3_path):
        self.ecm_html = s3_path
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

        audb.deployment_datetime = self._normalize_datetime(self.deployment_time)

        self._configure_provider_in_setup_block(audb, self.audience_provider)
        return audb

    def _crt_live_list_block(self, live_list):
        slb = None
        slb = WFEmailLiveSeedSendBlock() if self.is_created_from_onboarding \
            else WFEmailLiveSeedBlock()
        slb.seed_list_s3_path = live_list
        slb.campaign_name = "Live List - " + self.project_name
        slb.deployment_datetime = self._normalize_datetime(self.deployment_time)
        self._configure_provider_in_setup_block(slb, self.live_seeds_provider)
        return slb

    def _normalize_datetime(self, date_time):

        # if the datetime is Naive (hasnt timezone) assume that the tz is the current env tz
        if date_time.tzinfo is None or date_time.tzinfo.utcoffset(
                date_time) is None:
            date_time = date_time.replace(tzinfo=tz.tzlocal())

        return date_time.astimezone(tz.tzutc())

    def _check_viability(self):

        def check_not_none(name, value):
            if value is None:
                raise WFBrigeException("{} is required".format(name))

        if self.is_created_from_onboarding:
            check_not_none("ecm_html", self.ecm_html)
            check_not_none("html", self.html)
        else:
            if self.html is None and self.html_zip is None:
                err = "At least a zip or an html should be provided"
                raise WFBrigeException(err)

            if self.html is not None and self.html_zip is not None:
                err = "Only a zip or an html should be provided"
                raise WFBrigeException(err)

        check_not_none("subject", self.subject)
        check_not_none("email_creative_id", self.email_creative_id)

        check_not_none("audience_provider", self.audience_provider.name)
        check_not_none("audience_sender_name",
                       self.audience_provider.sender_name)
        check_not_none("audience_sender_email",
                       self.audience_provider.sender_email)

        check_not_none("add_tags_weight_approval_step", self.add_tags_weight_approval_step)

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
        project.email_creative_id = self.email_creative_id
        project.from_line = self.audience_provider.sender_name
        project.subject_test_prefix = self.subject_test_prefix
        project.deployment_time = self._normalize_datetime(self.deployment_time)
        project.project_id = self.project_id

        project.ttd_advertiser_id = self.ttd_advertiser_id
        project.ttd_bonus_media_advertiser_id = self.ttd_bonus_media_advertiser_id
        project.lr_account_id = self.lr_account_id
        project.lr_bonus_media_account_id = self.lr_bonus_media_account_id

        if self.is_created_from_onboarding:
            project.ecm_html = self.ecm_html
            project.html_s3_path = self.html
        else:
            zipb = WFEmailGenHtmlFromZipBlock()
            if self.html_zip is not None:
                zipb.zip_s3_path = self.html_zip
                project.html_s3_path = '-'
            else:
                zipb.zip_s3_path = '-'
                project.html_s3_path = self.html
            project.append(zipb)

        bval_html = WFEmailValidateHtmlBlock()
        bval_html.email_subject = self.subject
        project.append(bval_html)

        if self.audience_provider.name.lower() != 'ongage':
            if self.live_seed_list is not None:
                email_seed_block = self._crt_live_list_block(self.live_seed_list)
                project.append(email_seed_block)

            audb = self._crt_audience_block()
            project.append(audb)

            if not self.is_created_from_onboarding and self.add_tags_weight_approval_step:
                block_approve_cw_tags = WFEmailApproveCWTaggingBlock()
                project.append(block_approve_cw_tags)

            if self.review_deployment:
                reviewb = WFEmailReviewDeploymentBlock()
                project.append(reviewb)
        else:
            push_dwh_el = WFEmailPushToDWHAndEL()
            project.append(push_dwh_el)

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
        self.subject = None
        self.html = None
        self.category = None
        self.from_line = None
        self.suppression_file_path = None
        self.client_id = None
        self.email_creative_id = None

        self.__project = None

        self.seeds_provider = ProviderConfig()

    def set_html(self, s3_path):
        self.html = s3_path
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

    def set_email_creative_id(self, id):
        self.email_creative_id = id
        return self

    def _check_viability(self):

        def check_not_none(name, value):
            if value is None:
                raise WFBrigeException("{} is required".format(name))

        def check_file_extension(name, file_name, allowed_extensions=(".html",)):
            if not file_name.lower().endswith(allowed_extensions):
                raise WFBrigeException(
                    "{}: {} file hasn't an allowed extensions ({})".format(name, file_name,
                                                                           ",".join(allowed_extensions)))

        check_not_none("subject", self.subject)
        check_not_none("email_creative_id", self.email_creative_id)
        check_not_none("html", self.html)
        check_file_extension("html", self.html, (".html", ".zip"))
        check_not_none("category", self.category)
        check_not_none("from_line", self.from_line)
        check_file_extension("live_seed_list", self.live_seed_list, (".csv",))

        if self.suppression_file_path is not None and self.suppression_file_path:
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

    def _configure_provider_in_setup_block(self, block, provider):
        block.sender_email = provider.sender_email
        block.sender_name = provider.sender_name

        block.provider = provider.name
        block.provider_user = provider.user
        block.provider_password = provider.password
        block.provider_token = provider.token

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

        project.tags = "onboarding"
        project.email_subject = self.subject
        project.from_line = self.from_line
        project.suppression_file_path = self.suppression_file_path
        project.client_id = self.client_id
        project.category = self.category
        project.email_creative_id = self.email_creative_id

        if self.html.lower().endswith(".zip"):
            zipb = WFEmailGenHtmlFromZipBlock()
            zipb.zip_s3_path = self.html
            project.append(zipb)
        else:
            project.html_s3_path = self.html

        bval_html = WFEmailValidateHtmlBlock()
        bval_html.email_subject = self.subject
        project.append(bval_html)

        email_live_seed_block = WFEmailLiveSeedValidateBlock()
        email_live_seed_block.seed_list_s3_path = self.live_seed_list

        project.live_seed_list = self.live_seed_list

        project.append(email_live_seed_block)

        wf_project = parser.create(project)

        wf_project.set_fields({"portfolioID": self.client_id})

        return wf_project
