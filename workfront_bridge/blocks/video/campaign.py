from workfront_bridge.blocks.display.campaign import WFDisplayCampaignBlock


class WFVideoCampaignBlock(WFDisplayCampaignBlock):
    """
    @summary: Video Campaign block
    """

    def __init__(self):
        super(WFVideoCampaignBlock, self).__init__()
        self.automation_type = 'VideoCampaignCreate'
