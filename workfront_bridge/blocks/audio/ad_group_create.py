from workfront_bridge.blocks.display.ad_group_create import WFDisplayCreateAdGroupBlock


class WFAudioCreateAdGroupBlock(WFDisplayCreateAdGroupBlock):
    """
    @summary: Audio Create Ad Group block
    """

    def __init__(self):
        super(WFAudioCreateAdGroupBlock, self).__init__()
        self.automation_type = 'AudioAdGroupCreate'
