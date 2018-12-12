from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.blocks.social.creative_image import WFSocialCreativeImageBlock
from workfront_bridge.blocks.social.creative_video import WFSocialCreativeVideoBlock
from workfront_bridge.blocks.social.creative_carousel_ss_create import WFSocialCreativeCarouselSlideshowCreateBlock
from workfront_bridge.tools import set_kwargs


class WFSocialCreativeCarouselSlideshowSetupBlock(WFBlock):
    """
    @summary: Social Creative Carousel / Slideshow Setup block
    """

    template_name = 'Block - Social Carousel/Slideshow Setup'
    # create_carousel_slideshow_task_name = 'Create Creative Carousel/Slideshow'
    max_assets = 10

    def __init__(self):
        super(WFSocialCreativeCarouselSlideshowSetupBlock, self).__init__(self.template_name)
        self._assets = []

    def add_asset(self, **kwargs):
        if len(self._assets) == self.max_assets:
            raise WFBrigeException('The maximum number of creatives for a Carousel or Slideshow is {}'
                                   .format(self.max_assets))
        type_to_block = {
            'image': WFSocialCreativeImageBlock,
            'video': WFSocialCreativeVideoBlock,
        }
        AssetBlockClass = type_to_block[kwargs['asset_type']]
        asset = AssetBlockClass()
        asset = set_kwargs(asset, kwargs, exclude=['asset_type'])
        self._assets.append(asset)
        self.append(asset)

    def add_carousel_or_slideshow(self, **kwargs):
        creative = WFSocialCreativeCarouselSlideshowCreateBlock()
        creative = set_kwargs(creative, kwargs, exclude=['creative_type', 'asset_type', 'assets'])
        self.append(creative)
