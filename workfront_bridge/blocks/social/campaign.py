from workfront_bridge.blocks.base import WFBlock


class WFSocialSetupBlock(WFBlock):
    """
    @summary: Social Setup block. Campaign information.
    """

    template_name = 'Block - Social Setup'

    def __init__(self):
        super(WFSocialSetupBlock, self).__init__(self.template_name)
        self._set_starter_task(2)