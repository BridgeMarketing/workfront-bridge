from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.tools import datetime_to_wf_format


class WFResumeEmailDeployBlock(WFBlock):
    '''
    @summary: Use this block to resume the deploy to an esp of an email project.
    This block contains a single automatic task called "Resume Email Deploy"
    that will be excecuted in the Campaign Manager and will make the deploy of
    the emails resume(if needed).
    '''

    template_name = 'Block - Resume Email Deploy'

    block_params = {
        'Resume Email Deploy': [
            ('wf_email_project_id', 'project_id', True),
            ('Deployment Date/Time', 'deploy_datetime', True, datetime_to_wf_format),
        ],
    }


class WFResumeMediaCampaignDeployBlock(WFBlock):
    '''
    @summary: Use this block to resume the deploy of Audio/Video/Display
    project.
    This block contains a single automatic task called "Resume Media Campaign
    Deploy" that will be executed in the Campaign Manager and will resume the
    deploy of the media.
    '''

    template_name = 'Block - Resume Media Campaign Deploy'

    block_params = {
        'Resume Media Campaign Deploy': [
            ('wf_email_project_id', 'project_id', True),
            ('Deployment Date/Time', 'deploy_datetime', True, datetime_to_wf_format),
            ('End Date/Time', 'end_datetime', True, datetime_to_wf_format),
        ],
    }
