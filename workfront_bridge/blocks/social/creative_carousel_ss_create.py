from workfront_bridge.blocks.base import WFBlock


class WFSocialCreativeCarouselSlideshowCreateBlock(WFBlock):
    """
    @summary: Social Carousel/Slideshow Create block.
    """

    template_name = 'Block - Social Carousel/Slideshow Create'
    task_name = 'Carousel/Slideshow Create'

    def __init__(self):
        super(WFSocialCreativeCarouselSlideshowCreateBlock, self).__init__(self.template_name)
        self._add_required_parameters([
            'Social Carousel/Slideshow',
        ])
        self._add_optional_parameters([
            'Social Creative Message',
            'Social Advertiser Website URL',
            'FB/Instagram Call to Action',
        ])
        self._carousel_or_slideshow = None
        self._message = None
        self._advertiser_website_url = None
        self._fb_call_to_action = None

    @property
    def carousel_or_slideshow(self):
        return self._carousel_or_slideshow

    @carousel_or_slideshow.setter
    def carousel_or_slideshow(self, v):
        self._carousel_or_slideshow = v
        self.set_parameter(self.task_name, 'Social Carousel/Slideshow', v.capitalize())

    @property        
    def message(self):
        return self._message
    
    @message.setter
    def message(self, v):
        self._message = v
        self.set_parameter(self.task_name, 'Social Creative Message', v)

    @property        
    def advertiser_website_url(self):
        return self._advertiser_website_url
    
    @advertiser_website_url.setter
    def advertiser_website_url(self, v):
        self._advertiser_website_url = v
        self.set_parameter(self.task_name, 'Social Advertiser Website URL', v)

    @property        
    def fb_call_to_action(self):
        return self._fb_call_to_action
    
    @fb_call_to_action.setter
    def fb_call_to_action(self, v):
        self._fb_call_to_action = v
        self.set_parameter(self.task_name, 'FB/Instagram Call to Action', v)
