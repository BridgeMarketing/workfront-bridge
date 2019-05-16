from workfront_bridge.blocks.display.ad_group_create import WFDisplayCreateAdGroupBlock


class WFVideoCreateAdGroupBlock(WFDisplayCreateAdGroupBlock):
    """
    @summary: Video Create Ad Group block
    """

    def __init__(self):
        super(WFVideoCreateAdGroupBlock, self).__init__()
        self.automation_type = 'VideoAdGroupCreate'
