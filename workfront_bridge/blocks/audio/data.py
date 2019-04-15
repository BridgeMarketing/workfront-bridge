from workfront_bridge.blocks.display.data import WFDisplayDataBlock


class WFAudioDataBlock(WFDisplayDataBlock):
    """
    @summary: Audio Data block
    """

    def __init__(self):
        super(WFAudioDataBlock, self).__init__()

        # setting default value to Audio
        self.automation_type = 'AudioAudienceCreate'
