from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.blocks.display.creative_upload import WFDisplayCreativeUploadBlock


class WFDisplaySetupBlock(WFBlock):
    """
    @summary: Display Setup block
    """

    template_name = 'Block - Display Setup'

    def __init__(self):
        super(WFDisplaySetupBlock, self).__init__(self.template_name)
        self.append(WFDisplayCreativeUploadBlock())
        self.append(WFDisplayCreativeUploadBlock())

