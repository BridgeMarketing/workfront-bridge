from workfront_bridge.blocks.base import WFBlock


class HygieneDataBlock(WFBlock):
    """
    @summary: Hygiene process block
    """

    template_name = 'Block - Data - Hygiene'

    def __init__(self):
        super(HygieneDataBlock, self).__init__(self.template_name)
