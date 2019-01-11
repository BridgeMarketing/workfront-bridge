from workfront_bridge.blocks.base import WFBlock


class WFPauseEmailDeployBlock(WFBlock):
    '''
    @summary: Use this block to pause the deploy to an esp of an email project.
    This block contains a single automatic task called "Pause Email Deploy"
    that will be excecuted in the Campaign Manager and will make the deploy of
    the emails pause(if needed).
    '''

    template_name = 'Block - Pause Email Deploy'

    def __init__(self):
        super(WFPauseEmailDeployBlock, self).__init__(self.template_name)

        req = ["wf_email_project_id"]
        self._add_required_parameters(req)

        # Block Fields :
        self._wf_project_id = None

    @property
    def project_id(self):
        return self._wf_project_id

    @project_id.setter
    def project_id(self, wpid):
        '''
        @summary: WF id of the project being paused
        '''
        self._wf_project_id = wpid
        self.set_parameter("Pause Email Deploy", "wf_email_project_id", wpid)
