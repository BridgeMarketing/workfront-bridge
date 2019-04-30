from workfront_bridge.blocks.display.campaign import WFDisplayCampaignBlock


class WFAudioCampaignBlock(WFDisplayCampaignBlock):
    """
    @summary: Audio Campaign block
    """

    def __init__(self):
        super(WFAudioCampaignBlock, self).__init__()
        self.automation_type = 'AudioCampaignCreate'
