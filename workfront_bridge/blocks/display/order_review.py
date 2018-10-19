from workfront_bridge.blocks.base import WFBlock


class WFDisplayOrderReviewBlock(WFBlock):
    """
    @summary: Display Order Review block
    """

    template_name = 'Block - Display Order Review'

    def __init__(self):
        super(WFDisplayOrderReviewBlock, self).__init__(self.template_name)
