from workfront_bridge.blocks.base import WFBlock


class WFCancelEmailDeployBlock(WFBlock):
    '''
    @summary: Use this block to cancel the deploy to an esp of an email project.
    This block contains a single automatic task called "Cancel Email Deploy"
    that will be excecuted in the Campaign Manager and will make the deploy of
    the emails stop(if needed).
    '''

    template_name = 'Block - Cancel Email Deploy'

    def __init__(self):
        super(WFCancelEmailDeployBlock, self).__init__(self.template_name)

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
        @summary: WF id of the project being cancelled
        '''
        self._wf_project_id = wpid
        self.set_parameter("Cancel Email Deploy", "wf_email_project_id", wpid)
