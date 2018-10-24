from workfront_bridge.blocks.base import WFBlock


class EventLoopSetupBlock(WFBlock):
    """
    @summary: Event Loop Setup block for Target Bonus Media channels
    """

    template_name = 'Block - Event Loop Setup'

    def __init__(self):
        super(EventLoopSetupBlock, self).__init__(self.template_name)
