from workfront_bridge.blocks.base import WFBlock


class WFPauseEmailDeployBlock(WFBlock):
    '''
    @summary: Use this block to pause the deploy to an esp of an email project.
    This block contains a single automatic task called "Pause Email Deploy"
    that will be executed in the Campaign Manager and will make the deploy of
    the emails pause(if needed).
    '''

    template_name = 'Block - Pause Email Deploy'

    block_params = {
        'Pause Email Deploy': [
            ('wf_email_project_id', 'project_id', True),
        ],
    }


class WFPauseDisplayDeployBlock(WFBlock):
    '''
    @summary: Use this block to pause the deploy to an ttd of an display project.
    This block contains a single automatic task called "Pause Display Deploy"
    that will be executed in the Campaign Manager and will make the deploy of
    the display pause(if needed).
    '''

    template_name = 'Block - Pause Display Deploy'

    block_params = {
        'Pause Email Deploy': [
            ('data_v1', 'data', True),
        ],
    }
