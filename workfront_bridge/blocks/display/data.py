from workfront_bridge.blocks.base import WFBlock


class WFDisplayDataBlock(WFBlock):
    """
    @summary: Display Data block
    """

    template_name = 'Block - Display Data'

    def __init__(self):
        super(WFDisplayDataBlock, self).__init__(self.template_name)
