from workfront_bridge.blocks.base import WFBlock


class WFEmailTestSeedNoEmailSentBlock(WFBlock):
    '''
    @summary: Use this block to validate seed lists using the CCM (without
    sending emails).
    This block contains a Test Setup block that has validate seed
    list task and seed list approval task.
    '''

    template_name = 'Block - Email Test Setup (no emails sent)'

    def __init__(self):
        super(WFEmailTestSeedNoEmailSentBlock, self).__init__(self.template_name)

        req = ["cm_test_aud_s3_path"]
        self._add_required_parameters(req)

        # Block Fields :
        self._seed_list_path = None
        self._set_starter_task(2)

    @property
    def seed_list_s3_path(self):
        return self._seed_list_path

    @seed_list_s3_path.setter
    def seed_list_s3_path(self, sl):
        self._seed_list_path = sl
        self.set_parameter("Test Setup", "cm_test_aud_s3_path", sl)


class WFEmailValidateHtmlBlock(WFBlock):
    '''
    @summary: Use this block to validate an html with the CCM.
    This block will add validate html and creative approval task.
    '''

    template_name = 'Block - Email Validate Html'

    def __init__(self):
        super(WFEmailValidateHtmlBlock, self).__init__(self.template_name)

        req = ["ecm_email_subject"]
        self._add_required_parameters(req)

        # Block Fields :
        self._email_subject = None

    @property
    def email_subject(self):
        return self._email_subject

    @email_subject.setter
    def email_subject(self, v):
        self._email_subject = v
        self.set_parameter("Validate HTML", "ecm_email_subject", v)


class WFEmailGenHtmlFromZipBlock(WFBlock):
    '''
    @summary: Use this block to generate an html from a zip file.
    This block will add the generate html from zip task.
    '''

    template_name = 'Block - Email Generate Html from zip'

    def __init__(self):
        super(WFEmailGenHtmlFromZipBlock, self).__init__(self.template_name)

        req = ["ecm_zip"]
        self._add_required_parameters(req)

        # Block Fields:
        self._zip_s3_path = None

    @property
    def zip_s3_path(self):
        return self._zip_s3_path

    @zip_s3_path.setter
    def zip_s3_path(self, v):
        self._zip_s3_path = v
        self.set_parameter("Generate HTML from zip", "ecm_zip", v)


class WFEmailTestSeedBlock(WFBlock):
    '''
    @summary: Use this block to validate seed lists using the CCM and send test
    emails (wiht the seed list) using the CM.
    This block contains a Test Setup block that has this tasks:
    - Validate Seed List (CCM)
    - Upload Audience (CM)
    - Upload Creative (CM)
    - Create Flight (CM)
    - Push to provider (CM)
    - Seed List Approval (CCM)
    '''

    template_name = 'Block - Email Test Setup'

    def __init__(self):
        super(WFEmailTestSeedBlock, self).__init__(self.template_name)

        req = ["cm_test_aud_s3_path", "Campaign Name", "Sender Name",
               "Deployment Date/Time", "Sender Email"]
        self._add_required_parameters(req)

        opt = ["SelectedProvider", "Email Provider User",
               "Email Provider Password", "Email Provider Token"]
        self._add_optional_parameters(opt)

        # Block Fields:
        self._seed_list_path = None
        self._campaign_name = None
        self._sender_name = None
        self._sender_email = None
        self._deployment_datetime = None
        self._provider = None
        self._provider_user = None
        self._provider_password = None
        self._provider_token = None

        self._set_starter_task(2)  # Skip Test Setup

    @property
    def seed_list_s3_path(self):
        return self._seed_list_path

    @seed_list_s3_path.setter
    def seed_list_s3_path(self, sl):
        self._seed_list_path = sl
        self.set_parameter("Test Setup", "cm_test_aud_s3_path", sl)

    @property
    def campaign_name(self):
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, name):
        self._campaign_name = name
        self.set_parameter("Create Flight", "Campaign Name", name)

    @property
    def sender_email(self):
        return self._sender_email

    @sender_email.setter
    def sender_email(self, email):
        self._sender_email = email
        self.set_parameter("Create Flight", "Sender Email", email)

    @property
    def sender_name(self):
        return self._sender_name

    @sender_name.setter
    def sender_name(self, name):
        self._sender_name = name
        self.set_parameter("Create Flight", "Sender Name", name)

    @property
    def deployment_datetime(self):
        return self._deployment_datetime

    @deployment_datetime.setter
    def deployment_datetime(self, date_time):
        '''
        @param date_time: datetime object.
        '''
        self._deployment_datetime = date_time
        self.set_parameter("Create Flight", "Deployment Date/Time",
                           date_time.strftime("%d/%m/%Y %H:%M"))

    @property
    def provider(self):
        return self._provider

    @provider.setter
    def provider(self, provider):
        self._provider = provider
        self.set_parameter("Push to provider", "SelectedProvider", provider)

    @property
    def provider_user(self):
        return self._provider_user

    @provider_user.setter
    def provider_user(self, provider_user):
        self._provider_user = provider_user
        self.set_parameter("Push to provider", "Email Provider User",
                           provider_user)

    @property
    def provider_password(self):
        return self._provider_password

    @provider_password.setter
    def provider_password(self, provider_pass):
        self._provider_password = provider_pass
        self.set_parameter("Push to provider", "Email Provider Password",
                           provider_pass)

    @property
    def provider_token(self):
        return self._provider_token

    @provider_token.setter
    def provider_token(self, provider_token):
        self._provider_token = provider_token
        self.set_parameter("Push to provider", "Email Provider Token",
                           provider_token)


class WFEmailLiveSeedBlock(WFBlock):
    '''
    @summary: Use this block to validate live seed lists using the CCM (without
    sending emails).
    This block contains a Live Setup block that has validate seed
    list task and seed list approval task.
    '''

    template_name = 'Block - Email Live Setup'

    def __init__(self):
        super(WFEmailLiveSeedBlock, self).__init__(self.template_name)

        req = ["live_seed_list_s3_path"]
        self._add_required_parameters(req)

        # Block Fields :
        self._seed_list_path = None

        self._set_starter_task(2)  # Skip Live Setup

    @property
    def seed_list_s3_path(self):
        return self._seed_list_path

    @seed_list_s3_path.setter
    def seed_list_s3_path(self, sl):
        self._seed_list_path = sl
        self.set_parameter("Live Setup", "live_seed_list_s3_path", sl)


class WFEmailAudienceLiveSetupBlock(WFBlock):
    '''
    @summary: Use this block to send emails to the audience in the program of
    the project using the CM
    This block contains a Audience Live Setup block that has this tasks:
    - Upload Audience (CM)
    - Upload Creative (CM)
    - Create Flight (CM)
    - Push to provider (CM)
    '''

    template_name = 'Block - Email Audience Live Setup'

    def __init__(self):
        super(WFEmailAudienceLiveSetupBlock, self).__init__(self.template_name)

        req = ["cm_aud_s3_path", "Campaign Name", "Sender Name",
               "Deployment Date/Time", "Sender Email"]
        self._add_required_parameters(req)

        opt = ["SelectedProvider", "Email Provider User",
               "Email Provider Password", "Email Provider Token"]
        self._add_optional_parameters(opt)

        # Block Fields:
        self._seed_list_path = None
        self._campaign_name = None
        self._sender_name = None
        self._sender_email = None
        self._deployment_datetime = None
        self._provider = None
        self._provider_user = None
        self._provider_password = None
        self._provider_token = None

        self._set_starter_task(2)  # Skip Test Setup

    @property
    def seed_list_s3_path(self):
        return self._seed_list_path

    @seed_list_s3_path.setter
    def seed_list_s3_path(self, sl):
        self._seed_list_path = sl
        self.set_parameter("Audience Live Setup", "cm_aud_s3_path", sl)

    @property
    def campaign_name(self):
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, name):
        self._campaign_name = name
        self.set_parameter("Create Flight", "Campaign Name", name)

    @property
    def sender_email(self):
        return self._sender_email

    @sender_email.setter
    def sender_email(self, email):
        self._sender_email = email
        self.set_parameter("Create Flight", "Sender Email", email)

    @property
    def sender_name(self):
        return self._sender_name

    @sender_name.setter
    def sender_name(self, name):
        self._sender_name = name
        self.set_parameter("Create Flight", "Sender Name", name)

    @property
    def deployment_datetime(self):
        return self._deployment_datetime

    @deployment_datetime.setter
    def deployment_datetime(self, date_time):
        '''
        @param date_time: datetime object.
        '''
        self._deployment_datetime = date_time
        self.set_parameter("Create Flight", "Deployment Date/Time",
                           date_time.strftime("%d/%m/%Y %H:%M"))

    @property
    def provider(self):
        return self._provider

    @provider.setter
    def provider(self, provider):
        self._provider = provider
        self.set_parameter("Push to provider", "SelectedProvider", provider)

    @property
    def provider_user(self):
        return self._provider_user

    @provider_user.setter
    def provider_user(self, provider_user):
        self._provider_user = provider_user
        self.set_parameter("Push to provider", "Email Provider User",
                           provider_user)

    @property
    def provider_password(self):
        return self._provider_password

    @provider_password.setter
    def provider_password(self, provider_pass):
        self._provider_password = provider_pass
        self.set_parameter("Push to provider", "Email Provider Password",
                           provider_pass)

    @property
    def provider_token(self):
        return self._provider_token

    @provider_token.setter
    def provider_token(self, provider_token):
        self._provider_token = provider_token
        self.set_parameter("Push to provider", "Email Provider Token",
                           provider_token)


class WFEmailReviewDeploymentBlock(WFBlock):
    '''
    @summary: Use this block to add a non automatic task to review the
    deployment of the email by a human.
    '''

    template_name = 'Block - Email Review Deployment'

    def __init__(self):
        super(WFEmailReviewDeploymentBlock, self).__init__(self.template_name)

        self._set_starter_task(2)  # Skip Deploy group tast
