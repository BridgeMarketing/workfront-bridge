from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.blocks.social.ad_group_create import WFSocialAdGroupCreateBlock
from workfront_bridge.blocks.social.creative_image import WFSocialCreativeImageBlock
from workfront_bridge.tools import set_kwargs


class WFSocialAdGroupSetupBlock(WFBlock):
    """
    @summary: Social Ad Group Setup block. (Ad Set for Facebook)
    """

    template_name = 'Block - Social Ad Group Setup Setup'

    def __init__(self):
        super(WFSocialAdGroupSetupBlock, self).__init__(self.template_name)

    def add_creative(self, **kwargs):
        image = WFSocialCreativeImageBlock()
        image = set_kwargs(image, kwargs, exclude=['creative_type'])
        self.append(image)

    def add_ad_group(self, **kwargs):
        ad_group = WFSocialAdGroupCreateBlock()
        ad_group = set_kwargs(ad_group, kwargs, exclude=['creatives'])
        self.append(ad_group)
