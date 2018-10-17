from workfront_bridge.blocks.base import WFBlock


class WFDisplayCreativeUploadBlock(WFBlock):
    """
    @summary: Display Creative Upload block
    """

    template_name = 'Block - Display Creative Upload'

    def __init__(self):
        super(WFDisplayCreativeUploadBlock, self).__init__(self.template_name)
