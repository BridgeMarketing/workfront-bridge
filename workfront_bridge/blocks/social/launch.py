from workfront_bridge.blocks.base import WFBlock


class WFSocialLaunchBlock(WFBlock):
    """
    @summary: Social Setup block. Campaign information.
    """

    template_name = 'Block - Social Launch'
    launch_task_name = 'Launch'

    def __init__(self):
        super(WFSocialLaunchBlock, self).__init__(self.template_name)
        self._set_starter_task(2)
        self._add_required_parameters([
            'Social Provider'
        ])
        self._provider = None

    @property
    def provider(self):
        return self._provider

    @provider.setter
    def provider(self, v):
        self._provider = v
        self.set_parameter(self.launch_task_name, 'Social Provider', v)
