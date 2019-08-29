from workfront_bridge.blocks.base import WFBlock


class MergeDataBlock(WFBlock):
    """
    @summary: Merge process block
    """

    template_name = 'Block - Data - Merge'

    def __init__(self):
        super(MergeDataBlock, self).__init__(self.template_name)
