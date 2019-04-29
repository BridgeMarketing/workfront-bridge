from workfront_bridge.blocks.base import WFBlock


class WFCancelEmailDeployBlock(WFBlock):
    '''
    @summary: Use this block to cancel the deploy to an esp of an email project.
    This block contains a single automatic task called "Cancel Email Deploy"
    that will be excecuted in the Campaign Manager and will make the deploy of
    the emails stop(if needed).
    '''

    template_name = 'Block - Cancel Email Deploy'

    block_params = {
        'Cancel Email Deploy': [
            ('wf_email_project_id', 'project_id', True),
        ],
    }
