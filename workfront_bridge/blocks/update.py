from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.tools import datetime_to_wf_format


class WFUpdateEmailDeployBlock(WFBlock):
    '''
    @summary: Use this block to update the deploy to an esp of an email project.
    This block contains a single automatic task called "Update Email Deploy"
    that will be excecuted in the Campaign Manager and will make the deploy of
    the emails updated.
    '''

    template_name = 'Block - Update Email Deploy'

    block_params = {
        'Update Email Deploy': [
            ('wf_email_project_id', 'project_id', True),
            ('Deployment Date/Time', 'deploy_datetime', True, datetime_to_wf_format),
        ],
    }


class WFUpdateMediaDeployBlock(WFBlock):
    """
    @summary: Use this block to update the deploy of a Media project.
    """

    template_name = 'Block - Update Media Campaign Deploy'

    block_params = {
        'Update Media Campaign Deploy': [
            ('data_update', 'data', True),
        ],
    }
