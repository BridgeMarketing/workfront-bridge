from workfront_bridge.blocks.base import WFBlock


class WFSocialDataBlock(WFBlock):
    """
    @summary: Social Data block. Audience information.
    """

    template_name = 'Block - Social Data'

    def __init__(self):
        super(WFSocialDataBlock, self).__init__(self.template_name)
        self._set_starter_task(2)
