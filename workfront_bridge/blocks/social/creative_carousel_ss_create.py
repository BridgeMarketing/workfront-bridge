from workfront_bridge.blocks.base import WFBlock


class WFSocialCreativeCarouselSlideshowCreateBlock(WFBlock):
    """
    @summary: Social Carousel/Slideshow Create block.
    """

    template_name = 'Block - Social Carousel/Slideshow Create'

    block_params = {
        'Carousel/Slideshow Create': [
            ('Social Carousel/Slideshow', 'carousel_or_slideshow', True, lambda v: v.capitalize()),
            ('Social Creative Message', 'message', False),
            ('Social Advertiser Website URL', 'advertiser_website_url', False),
            ('FB/Instagram Call to Action', 'fb_call_to_action', False),
        ],
    }
