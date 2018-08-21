import sys

from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.projects.email import WFProjectEmailContainer
from workfront_bridge.blocks.email import WFEmailTestSeedNoEmailSentBlock, WFEmailLiveSeedBlock
from workfront_bridge.blocks.email import WFEmailTestSeedBlock
from workfront_bridge.blocks.email import WFEmailGenHtmlFromZipBlock
from workfront_bridge.blocks.email import WFEmailValidateHtmlBlock


#
# class EmailProjectBuilder(object):
#     '''
#     @summary: Email project builder to easily construct email workfront
#     projects.
#     '''
#
#     def __init__(self, wf, project_name):
#         '''
#         @param wf: Workfront service object
#         @param project_name: that the created will have.
#         '''
#         self.project_name = project_name
#         self.wf = wf
#         self.live_seed_list = None
#         self.test_seed_lists = []
#         self.subject = None
#         self.html = None
#         self.html_zip = None
#         self.provider = None
#         self.test_sl_send_emails = True
#
#     def set_html(self, s3_path):
#         self.html = s3_path
#         return self
#
#     def set_html_zip(self, s3_path):
#         self.html_zip = s3_path
#         return self
#
#     def add_test_list(self, s3_path):
#         self.test_seed_lists.append(s3_path)
#         return self
#
#     def set_seed_list(self, s3_path):
#         self.live_seed_list = s3_path
#         return self
#
#     def set_send_validate_test_seed_emails(self, val=True):
#         self.test_sl_send_emails = val
#         return self
#
#     def set_subject(self, subject):
#         self.subject = subject
#         return self
#
#     def set_provider(self, provider):
#         self.provider = provider
#         return self
#
#     def _check_viability(self):
#         if self.html is None and self.html_zip is None:
#             err = "At least a zip or an html should be provided"
#             raise WFBrigeException(err)
#
#         if self.html is not None and self.html_zip is not None:
#             err = "Only a zip or an html should be provided"
#             raise WFBrigeException(err)
#
#         def check_not_none(name, value):
#             if value is None:
#                 raise WFBrigeException("{} is required".format(name))
#
#         check_not_none("subject", self.subject)
#
#     def build(self):
#         '''
#         @summary: According to all the parameters set to the builder, build a
#         workfront project.
#         @raise WFBrigeException: if the combination of parameters set in the
#         builder are not compatible (like missing parameters).
#         @return: a WFProject object.
#         '''
#         self._check_viability()
#
#         pb = WFProjectEmailContainer(self.wf, self.project_name)
#         pb.email_subject = self.subject
#
#         if self.html_zip is not None:
#             zipb = WFEmailGenHtmlFromZipBlock(self.wf)
#             zipb.zip_s3_path = self.html_zip
#             pb.append(zipb)
#         else:
#             pb.html_s3_path = self.html
#
#         bval_html = WFEmailValidateHtmlBlock(self.wf)
#         bval_html.email_subject = self.subject
#         pb.append(bval_html)
#
#         for test_list in self.test_seed_lists:
#             if self.test_sl_send_emails:
#                 slb = WFEmailTestSeedBlock(self.wf)
#                 slb.seed_list_s3_path = test_list
#                 # TODO Fullfill other values
#             else:
#                 slb = WFEmailTestSeedNoEmailSentBlock(self.wf)
#                 slb.seed_list_s3_path = test_list
#             pb.append(slb)
#
#         if self.live_seed_list is not None:
#             email_seed_block = WFEmailLiveSeedBlock(self.wf)
#             email_seed_block.seed_list_s3_path = self.live_seed_list
#
#         return pb.create()


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

        if not self.suppression_file_path is None:
            check_file_extension("suppression_file_path", self.suppression_file_path, (".csv",))

        check_not_none("client_id", self.client_id)

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

        bval_html = WFEmailValidateHtmlBlock(self.wf)
        bval_html.email_subject = self.subject
        project.append(bval_html)

        for test_list in self.test_seed_lists:
            slb = WFEmailTestSeedNoEmailSentBlock()
            slb.seed_list_s3_path = test_list
            project.append(slb)

        project.test_seed_lists = ",".join(self.test_seed_lists)

        email_live_seed_block = WFEmailLiveSeedBlock()
        email_live_seed_block.seed_list_s3_path = self.live_seed_list

        project.live_seed_list = self.live_seed_list

        project.append(email_live_seed_block)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        wf_project.set_fields({"portfolioID": self.client_id})

        return wf_project
