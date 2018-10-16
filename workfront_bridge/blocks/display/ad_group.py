from workfront_bridge.blocks.base import WFBlock


class WFDisplayAdGroupBlock(WFBlock):
    """
    @summary: Display Ad Group block
    """

    template_name = 'Block - Display Ad Group'

    def __init__(self):
        super(WFDisplayAdGroupBlock, self).__init__(self.template_name)
