from workfront_bridge.blocks.base import WFBlock


class WFSocialCreativeImageBlock(WFBlock):
    """
    @summary: Social Creative Image block
    """

    template_name = 'Block - Social Image'

    def __init__(self):
        super(WFSocialCreativeImageBlock, self).__init__(self.template_name)
