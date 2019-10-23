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


class WFResumeDisplayDeployBlock(WFBlock):
    '''
    @summary: Use this block to resume the deploy to an esp of an display project.
    This block contains a single automatic task called "Resume Email Deploy"
    that will be excecuted in the Campaign Manager and will make the deploy of
    the emails resume(if needed).
    '''

    template_name = 'Block - Resume Display Deploy'

    block_params = {
        'Resume Display Deploy': [
            ('wf_email_project_id', 'project_id', True),
            ('Deployment Date/Time', 'deploy_datetime', True, datetime_to_wf_format),
        ],
    }
