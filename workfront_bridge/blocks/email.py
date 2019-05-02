from workfront_bridge.blocks.base import WFBlock


class WFEmailTestSeedNoEmailSentBlock(WFBlock):
    '''
    @summary: Use this block to validate seed lists using the CCM (without
    sending emails).
    This block contains a Test Setup block that has validate seed
    list task and seed list approval task.
    '''

    template_name = 'Block - Email Test Setup (no emails sent)'

    block_params = {
        'Test Setup': [
            ('cm_test_aud_s3_path', 'seed_list_s3_path', True),
        ],
    }

    def __init__(self):
        super(WFEmailTestSeedNoEmailSentBlock, self).__init__(self.template_name)
        self._set_starter_task(2)


class WFEmailValidateHtmlBlock(WFBlock):
    '''
    @summary: Use this block to validate an html with the CCM.
    This block will add validate html and creative approval task.
    '''

    template_name = 'Block - Email Validate Html'

    block_params = {
        'Validate HTML': [
            ('ecm_email_subject', 'email_subject', True),
        ],
    }


class WFEmailGenHtmlFromZipBlock(WFBlock):
    '''
    @summary: Use this block to generate an html from a zip file.
    This block will add the generate html from zip task.
    '''

    template_name = 'Block - Email Generate Html from zip'

    block_params = {
        'Generate HTML from zip': [
            ('ecm_zip', 'zip_s3_path', True),
        ],
    }


class WFEmailSeedBlock(WFBlock):
    '''
    @summary: Common elements for test/live seed block.
    Please, check WFEmailTestSeedBlock and WFEmailLiveSeedBlock for more details
    '''

    block_params = {
        'Create Flight': [
            ('Campaign Name', 'campaign_name', True),
            ('Sender Name', 'sender_name', True),
            ('Deployment Date/Time', 'deployment_datetime', True, lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.000%z")),
            ('Sender Email', 'sender_email', True),
        ],
        'Push to provider': [
            ('SelectedProvider', 'provider', False),
            ('Email Provider User', 'provider_user', False),
            ('Email Provider Password', 'provider_password', False),
            ('Email Provider Token', 'provider_token', False),
            ('isTest', 'is_test', False),
        ],
    }

    def __init__(self, wf_template_name=None):
        super(WFEmailSeedBlock, self).__init__(wf_template_name)
        self._set_starter_task(2)  # Skip Setup


class WFEmailTestSeedBlock(WFEmailSeedBlock):
    '''
    @summary: Use this block to validate seed lists using the CCM and send test
    emails (with the seed list) using the CM.
    This block contains a Test Setup block that has this tasks:
    - Validate Seed List (CCM)
    - Upload Audience (CM)
    - Upload Creative (CM)
    - Create Flight (CM)
    - Push to provider (CM)
    - Seed List Approval (CCM)
    '''

    template_name = 'Block - Email Test Setup'

    block_params = {
        'Test Setup': [
            ('cm_test_aud_s3_path', 'seed_list_s3_path', True),
        ],
    }

    def __init__(self):
        super(WFEmailTestSeedBlock, self).__init__(self.template_name)
        self.is_test = "yes"


class WFEmailLiveSeedBlock(WFEmailSeedBlock):
    '''
    @summary: Use this block to validate seed lists using the CCM and send test
    emails (with the seed list) using the CM.
    This block contains a Live Setup block that has this tasks:
    - Validate Seed List (CCM)
    - Seed List Approval (CCM)
    - Validate Start Date (OMS)
    - Upload Audience (CM)
    - Upload Creative (CM)
    - Create Flight (CM)
    - Push to provider (CM)
    '''

    template_name = 'Block - Email Live Setup v4'

    block_params = {
        'Live Setup': [
            ('live_seed_list_s3_path', 'seed_list_s3_path', True),
        ],
    }


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

    block_params = {
        'Audience Live Setup': [
            ('cm_aud_s3_path', 'seed_list_s3_path', False),
        ],
        'Create Flight': [
            ('Campaign Name', 'campaign_name', True),
            ('Sender Name', 'sender_name', True),
            ('Deployment Date/Time', 'deployment_datetime', True, lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.000%z")),
            ('Sender Email', 'sender_email', True),
        ],
        'Push to provider': [
            ('SelectedProvider', 'provider', False),
            ('Email Provider User', 'provider_user', False),
            ('Email Provider Password', 'provider_password', False),
            ('Email Provider Token', 'provider_token', False),
        ],
    }

    def __init__(self):
        super(WFEmailAudienceLiveSetupBlock, self).__init__(self.template_name)
        # Skip Test Setup and Validate Start Date
        self._set_starter_task(2)


class WFEmailReviewDeploymentBlock(WFBlock):
    '''
    @summary: Use this block to add a non automatic task to review the
    deployment of the email by a human.
    '''

    template_name = 'Block - Email Review Deployment'

    def __init__(self):
        super(WFEmailReviewDeploymentBlock, self).__init__(self.template_name)
        self._set_starter_task(2)  # Skip Deploy group tast


class WFEmailApproveCWTaggingBlock(WFBlock):
    '''
    @summary: Use this block to add a non automatic task to Approve the
    CW Tagging by a human.
    '''

    template_name = 'Block - Email - Approve CW Tagging'
