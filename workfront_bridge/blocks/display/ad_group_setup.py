from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.blocks.display.ad_group_creative_upload import WFDisplayCreativeUploadBlock
from workfront_bridge.blocks.display.ad_group_create import WFDisplayCreateAdGroupBlock
from workfront_bridge.tools import set_kwargs


class WFDisplayAdGroupSetupBlock(WFBlock):
    """
    @summary: Display Ad Group Setup block
    """

    template_name = 'Block - Display Ad Group Setup'

    def __init__(self):
        super(WFDisplayAdGroupSetupBlock, self).__init__(self.template_name)

    def add_creative(self, **kwargs):
        block_class = kwargs.pop('block_class', WFDisplayCreativeUploadBlock)
        creative = block_class()
        creative = set_kwargs(creative, kwargs)
        self.append(creative)

    def add_ad_group(self, **kwargs):
        block_class = kwargs.pop('block_class', WFDisplayCreateAdGroupBlock)
        ad_group = block_class()
        ad_group = set_kwargs(ad_group, kwargs, exclude=['creatives'])
        self.append(ad_group)
