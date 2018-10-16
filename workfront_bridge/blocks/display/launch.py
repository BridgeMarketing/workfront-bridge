from workfront_bridge.blocks.base import WFBlock


class WFDisplayLaunchBlock(WFBlock):
    """
    @summary: Display Launch block
    """

    template_name = 'Block - Display Launch'

    def __init__(self):
        super(WFDisplayLaunchBlock, self).__init__(self.template_name)
