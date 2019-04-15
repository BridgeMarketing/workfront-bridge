from workfront_bridge.blocks.base import WFBlock


class WFDisplayDataBlock(WFBlock):
    """
    @summary: Display Data block
    """

    template_name = 'Block - Display Data'

    def __init__(self):
        super(WFDisplayDataBlock, self).__init__(self.template_name)

        self._add_required_parameters([
            "Audience Name",
            "type",
        ])
        self._audience_name = None

        self._set_starter_task(2)

        # setting default value to Display
        self.automation_type = 'DigitalAudienceCreate'

    @property
    def automation_type(self):
        return self._automation_type

    @automation_type.setter
    def automation_type(self, v):
        self._automation_type = v
        self.set_parameter("Create Audience", "type", v)

    @property
    def audience_name(self):
        return self._audience_name

    @audience_name.setter
    def audience_name(self, v):
        self._audience_name = v
        self.set_parameter("Create Audience", "Audience Name", v)
