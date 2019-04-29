from workfront_bridge.blocks.base import WFBlock


class WFPauseEmailDeployBlock(WFBlock):
    '''
    @summary: Use this block to pause the deploy to an esp of an email project.
    This block contains a single automatic task called "Pause Email Deploy"
    that will be excecuted in the Campaign Manager and will make the deploy of
    the emails pause(if needed).
    '''

    template_name = 'Block - Pause Email Deploy'

    block_params = {
        'Pause Email Deploy': [
            ('wf_email_project_id', 'project_id', True),
        ],
    }
