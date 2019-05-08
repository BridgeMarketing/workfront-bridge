import pytz
from datetime import datetime

from workfront_bridge.blocks.email import WFEmailTestSeedBlockV2
from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.projects.email import WFProjectEmailContainer


class ProviderConfig(object):
    def __init__(self):
        self.name = None
        self.user = None
        self.password = None
        self.token = None
        self.sender_email = None
        self.sender_name = None


class EmailTestListProjectBuilder(object):
    '''
    @summary: Email test list project builder to easily construct
    email test list workfront projects.
    '''

    def __init__(self, wf, project_name):
        '''
        @param wf: Workfront service object
        @param project_name: that the created will have.
        '''

        self.project_name = project_name
        self.wf = wf
        self.test_seed_lists = None
        self.subject = None
        self.subject_test_prefix = None
        self.html = None
        self.html_zip = None
        self.provider = None
        self.email_creative_id = None

        self.seeds_provider = ProviderConfig()

        self.ecm_html = None

    def add_test_list(self, s3_path):
        self.test_seed_lists = s3_path
        return self

    def set_subject(self, subject):
        self.subject = subject
        return self

    def set_subject_test_prefix(self, subject_test_prefix):
        self.subject_test_prefix = subject_test_prefix
        return self

    def set_deployment_datetime(self, dt):
        self.deployment_time = dt
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

    def set_email_creative_id(self, id):
        self.email_creative_id = id
        return self

    def set_ecm_html(self, s3_path):
        self.ecm_html = s3_path
        return self

    def _check_viability(self):

        def check_not_none(name, value):
            if value is None:
                raise WFBrigeException("{} is required".format(name))

        check_not_none("ecm_html", self.ecm_html)

        check_not_none("subject", self.subject)
        check_not_none("email_creative_id", self.email_creative_id)

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
        @raise WFBridgeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        '''
        self._check_viability()

        project = WFProjectEmailContainer(self.project_name)

        project.email_subject = self.subject
        project.subject_test_prefix = self.subject_test_prefix
        project.email_creative_id = self.email_creative_id
        project.from_line = self.seeds_provider.sender_name

        project.ecm_html = self.ecm_html

        project.test_seed_lists = self.test_seed_lists

        sl_block = WFEmailTestSeedBlockV2()
        sl_block.seed_list_s3_path = self.test_seed_lists
        sl_block.campaign_name = "Test List - " + self.project_name
        sl_block.deployment_datetime = datetime.utcnow().replace(tzinfo=pytz.utc)
        self._configure_provider_in_setup_block(sl_block, self.seeds_provider)

        project.append(sl_block)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        return wf_project
