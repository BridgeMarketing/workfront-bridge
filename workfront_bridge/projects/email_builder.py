from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.projects.email import WFProjectEmailContainer
from workfront_bridge.blocks.email import WFEmailTestSeedNoEmailSentBlock
from workfront_bridge.blocks.email import WFEmailTestSeedBlock
from workfront_bridge.blocks.email import WFEmailGenHtmlFromZipBlock
from workfront_bridge.blocks.email import WFEmailValidateHtmlBlock


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
        self.prjoject_name = project_name
        self.wf = wf
        self.live_seed_list = None
        self.test_seed_lists = []
        self.subject = None
        self.html = None
        self.html_zip = None
        self.provider = None
        self.test_sl_send_emails = True

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

    def set_provider(self, provider):
        self.provider = provider
        return self

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

    def build(self):
        '''
        @summary: According to all the parameters set to the builder, build a
        workfront project.
        @raise WFBrigeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        '''
        self._check_viability()

        pb = WFProjectEmailContainer(self.wf, self.prjoject_name)
        pb.email_subject = self.subject

        if self.html_zip is not None:
            zipb = WFEmailGenHtmlFromZipBlock(self.wf)
            zipb.zip_s3_path = self.html_zip
            pb.append(zipb)
        else:
            pb.html_s3_path = self.html

        bval_html = WFEmailValidateHtmlBlock(self.wf)
        bval_html.email_subject = self.subject
        pb.append(bval_html)

        for test_list in self.test_seed_lists:
            if self.test_sl_send_emails:
                slb = WFEmailTestSeedBlock(self.wf)
                slb.seed_list_s3_path = test_list
                # TODO Fullfill other values
            else:
                slb = WFEmailTestSeedNoEmailSentBlock(self.wf)
                slb.seed_list_s3_path = test_list
            pb.append(slb)

        if self.live_seed_list is not None:
            # TODO add live seed list block.
            pass

        return pb.create()
