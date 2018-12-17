from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.blocks.social.ad_group_create import WFSocialAdGroupCreateBlock
from workfront_bridge.blocks.social.creative_image import WFSocialCreativeImageBlock
from workfront_bridge.blocks.social.creative_video import WFSocialCreativeVideoBlock
from workfront_bridge.blocks.social.creative_carousel_ss_setup import WFSocialCreativeCarouselSlideshowSetupBlock
from workfront_bridge.tools import set_kwargs


class WFSocialAdGroupSetupBlock(WFBlock):
    """
    @summary: Social Ad Group Setup block. (Ad Set for Facebook)
    """

    template_name = 'Block - Social Ad Group Setup'

    def __init__(self):
        super(WFSocialAdGroupSetupBlock, self).__init__(self.template_name)

    def add_creative(self, **kwargs):
        type_to_block = {
            'image': WFSocialCreativeImageBlock,
            'video': WFSocialCreativeVideoBlock,
            'carousel/slideshow': WFSocialCreativeCarouselSlideshowSetupBlock,
        }
        CreativeBlockClass = type_to_block[kwargs['creative_type']]
        creative = CreativeBlockClass()
        if kwargs['creative_type'] == 'carousel/slideshow':
            [creative.add_asset(**asset) for asset in kwargs['assets']]
            creative.add_carousel_or_slideshow(**kwargs)
        else:
            creative = set_kwargs(creative, kwargs, exclude=['creative_type', 'carousel_or_slideshow', 'assets'])
        self.append(creative)

    def add_ad_group(self, **kwargs):
        ad_group = WFSocialAdGroupCreateBlock()
        ad_group = set_kwargs(ad_group, kwargs, exclude=['creatives'])
        self.append(ad_group)
