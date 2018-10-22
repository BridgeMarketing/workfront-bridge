from workfront_bridge.blocks.base import WFBlock


class WFSocialCreativeVideoBlock(WFBlock):
    """
    @summary: Social Creative Video block
    """

    template_name = 'Block - Social Video'

    def __init__(self):
        super(WFSocialCreativeVideoBlock, self).__init__(self.template_name)
