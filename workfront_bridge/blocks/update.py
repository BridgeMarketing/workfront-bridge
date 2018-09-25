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

    def __init__(self):
        super(WFUpdateEmailDeployBlock, self).__init__(self.template_name)

        req = ["wf_email_project_id", "Deployment Date/Time"]
        self._add_required_parameters(req)

        # Block Fields :
        self._wf_project_id = None
        self._deploy_datetime = None

    @property
    def project_id(self):
        return self._wf_project_id

    @project_id.setter
    def project_id(self, wpid):
        '''
        @summary: WF id of the project being updated
        '''
        self._wf_project_id = wpid
        self.set_parameter("Update Email Deploy", "wf_email_project_id", wpid)

    @project_id.setter
    def deploy_datetime(self, dt):
        '''
        @summary: deploy datetime of the project being updated
        '''
        self._deploy_datetime = dt
        self.set_parameter('Update Email Deploy',
                           'Deployment Date/Time',
                           datetime_to_wf_format(dt))
