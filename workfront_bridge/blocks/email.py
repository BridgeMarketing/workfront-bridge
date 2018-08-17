from workfront_bridge.blocks.base import WFBlock, template_id_from_name


class WFEmailTestSeedNoEmailSentBlock(WFBlock):
    '''
    @summary: Use this block to validate seed lists using the CCM (without
    sending emails).
    This block contains a Test Setup block that has validate seed
    list task and seed list approval task.
    '''

    template_name = 'Block - Email Test Setup (no emails sent)'

    def __init__(self, wf):
        template_id = template_id_from_name(wf, self.template_name)
        super(WFEmailTestSeedNoEmailSentBlock, self).__init__(wf, template_id)

        req = ["cm_test_aud_s3_path"]
        self._set_required_fields(req)

        # Block Fields :
        self._seed_list_path = None
        self._set_starter_task(2)

    @property
    def seed_list_s3_path(self):
        return self._seed_list_path

    @seed_list_s3_path.setter
    def seed_list_s3_path(self, sl):
        self._seed_list_path = sl
        self.set_task_param_value("Test Setup", "cm_test_aud_s3_path", sl)


class WFEmailValidateHtmlBlock(WFBlock):
    '''
    @summary: Use this block to validate an html with the CCM.
    This block will add validate html and creative approval task.
    '''

    template_name = 'Block - Email Validate Html'

    def __init__(self, wf):
        template_id = template_id_from_name(wf, self.template_name)
        super(WFEmailValidateHtmlBlock, self).__init__(wf, template_id)

        req = ["ecm_email_subject"]
        self._set_required_fields(req)

        # Block Fields :
        self._email_subject = None

    @property
    def email_subject(self):
        return self._email_subject

    @email_subject.setter
    def email_subject(self, v):
        self._email_subject = v
        self.set_task_param_value("Validate HTML", "ecm_email_subject", v)


class WFEmailGenHtmlFromZipBlock(WFBlock):
    '''
    @summary: Use this block to generate an html from a zip file.
    This block will add the generate html from zip task.
    '''

    template_name = 'Block - Email Generate Html from zip'

    def __init__(self, wf):
        template_id = template_id_from_name(wf, self.template_name)
        super(WFEmailGenHtmlFromZipBlock, self).__init__(wf, template_id)

        req = ["ecm_zip"]
        self._set_required_fields(req)

        # Block Fields:
        self._zip_s3_path = None

    @property
    def zip_s3_path(self):
        return self._zip_s3_path

    @zip_s3_path.setter
    def zip_s3_path(self, v):
        self._zip_s3_path = v
        self.set_task_param_value("Generate HTML from zip", "ecm_zip", v)


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

    def __init__(self, wf):
        template_id = template_id_from_name(wf, self.template_name)
        super(WFEmailTestSeedBlock, self).__init__(wf, template_id)

        req = ["cm_test_aud_s3_path", "Campaign Name", "Sender Name",
               "Deployment Date/Time", "Sender Email"]
        self._set_required_fields(req)

        opt = ["SelectedProvider"]
        self._set_optional_fields(opt)

        # Block Fields:
        self._seed_list_path = None
        self._campaign_name = None
        self._sender_name = None
        self._sender_email = None
        self._deployment_datetime = None

        self._set_starter_task(2)  # Skip Test Setup

    @property
    def seed_list_s3_path(self):
        return self._seed_list_path

    @seed_list_s3_path.setter
    def seed_list_s3_path(self, sl):
        self._seed_list_path = sl
        self.set_task_param_value("Test Setup", "cm_test_aud_s3_path", sl)

    @property
    def campaign_name(self):
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, name):
        self._campaign_name = name
        self.set_task_param_value("Create Flight", "Campaign Name", name)

    @property
    def sender_email(self):
        return self._sender_email

    @sender_email.setter
    def sender_email(self, email):
        self._sender_email = email
        self.set_task_param_value("Create Flight", "Sender Email", email)

    @property
    def sender_name(self):
        return self._sender_name

    @sender_name.setter
    def sender_name(self, name):
        self._sender_name = name
        self.set_task_param_value("Create Flight", "Sender Name", name)

    @property
    def deployment_datetime(self):
        return self._deployment_datetime

    @deployment_datetime.setter
    def deployment_datetime(self, date_time):
        '''
        @param date_time: datetime object.
        '''
        self._deployment_datetime = date_time
        self.set_task_param_value("Create Flight", "Deployment Date/Time",
                                  date_time.strftime("%d/%m/%Y %H:%M"))


class WFEmailLiveSeedBlock(WFBlock):
    '''
    @summary: Use this block to validate live seed lists using the CCM (without
    sending emails).
    This block contains a Live Setup block that has validate seed
    list task and seed list approval task.
    '''

    template_name = 'Block - Email Live Setup'

    def __init__(self, wf):
        template_id = template_id_from_name(wf, self.template_name)
        super(WFEmailLiveSeedBlock, self).__init__(wf, template_id)

        req = ["live_seed_list_s3_path"]
        self._set_required_fields(req)

        # Block Fields :
        self._seed_list_path = None

        self._set_starter_task(2)  # Skip Live Setup

    @property
    def seed_list_s3_path(self):
        return self._seed_list_path

    @seed_list_s3_path.setter
    def seed_list_s3_path(self, sl):
        self._seed_list_path = sl
        self.set_task_param_value("Live Setup", "live_seed_list_s3_path", sl)
