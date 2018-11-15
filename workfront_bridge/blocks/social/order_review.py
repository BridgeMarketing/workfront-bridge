from workfront_bridge.blocks.base import WFBlock


class WFSocialOrderReviewBlock(WFBlock):
    """
    @summary: Social Order Review block
    """

    template_name = 'Block - Social Order Review'

    def __init__(self):
        super(WFSocialOrderReviewBlock, self).__init__(self.template_name)
