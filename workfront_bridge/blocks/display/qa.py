from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.blocks.display.qa_creative import WFDisplayCreativeQABlock
from workfront_bridge.blocks.display.qa_ad_group import WFDisplayQAAdGroupBlock
from workfront_bridge.tools import set_kwargs


class WFDisplayQABlock(WFBlock):
    """
    @summary: Display QA block
    """

    template_name = 'Block - Display QA'

    def add_creative(self, **kwargs):
        block_class = kwargs.pop('block_class', WFDisplayCreativeQABlock)
        creative = block_class()
        creative = set_kwargs(creative,
                              kwargs,
                              exclude=['creative_type'])
        self.append(creative)

    def add_ad_group(self, **kwargs):
        block_class = kwargs.pop('block_class', WFDisplayQAAdGroupBlock)
        ad_group = block_class()
        ad_group = set_kwargs(ad_group, kwargs, exclude=['creatives'])
        self.append(ad_group)
