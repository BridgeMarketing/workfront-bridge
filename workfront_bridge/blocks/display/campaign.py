from workfront_bridge.blocks.base import WFBlock


class WFDisplayCampaignBlock(WFBlock):
    """
    @summary: Display Campaign block
    """

    template_name = 'Block - Display Campaign'

    def __init__(self):
        super(WFDisplayCampaignBlock, self).__init__(self.template_name)
