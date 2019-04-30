from workfront_bridge.blocks.base import WFBlock


class WFDisplayDataBlock(WFBlock):
    """
    @summary: Display Data block
    """

    template_name = 'Block - Display Data'

    block_params = {
        'Create Audience': [
            ('Audience Name', 'audience_name', True),
            ('type', 'automation_type', True),
        ],
    }

    def __init__(self):
        super(WFDisplayDataBlock, self).__init__(self.template_name)
        self._set_starter_task(2)
        self.automation_type = 'DigitalAudienceCreate'
