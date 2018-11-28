from workfront_bridge.blocks.base import WFBlock


class WFReviewDataBlock(WFBlock):
    """
    @summary: Use this block to add a Review Data task in a data project.
    """

    template_name = 'Block - Data - Review Data'

    def __init__(self):
        super(WFReviewDataBlock, self).__init__(self.template_name)
