from workfront_bridge.blocks.base import WFBlock


class WFSocialCreativeCarouselSlideshowBlock(WFBlock):
    """
    @summary: Social Creative Carousel / Slideshow block
    """

    template_name = 'Block - Social Carousel/Slideshow'

    def __init__(self):
        super(WFSocialCreativeCarouselSlideshowBlock, self).__init__(self.template_name)