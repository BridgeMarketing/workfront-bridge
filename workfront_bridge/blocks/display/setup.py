from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.blocks.display.setup_creative_upload import WFDisplayCreativeUploadBlock
from workfront_bridge.exceptions import WFBrigeException


class WFDisplaySetupBlock(WFBlock):
    """
    @summary: Display Setup block
    """

    template_name = 'Block - Display Setup'

    def __init__(self):
        super(WFDisplaySetupBlock, self).__init__(self.template_name)

    def add_creative(self, **kwargs):
        creative = WFDisplayCreativeUploadBlock()
        for k, v in kwargs.items():
            try:
                getattr(creative, k)
            except AttributeError:
                raise WFBrigeException('Invalid Key: {}'.format(k))
            else:
                setattr(creative, k, v)
        self.append(creative)
