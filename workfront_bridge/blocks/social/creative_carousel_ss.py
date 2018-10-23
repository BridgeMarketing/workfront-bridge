from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.exceptions import WFBrigeException


class WFSocialCreativeCarouselSlideshowBlock(WFBlock):
    """
    @summary: Social Creative Carousel / Slideshow block
    """

    template_name = 'Block - Social Carousel/Slideshow'
    create_carousel_slideshow_task_name = 'Create Creative Carousel/Slideshow'
    max_creatives = 5

    def __init__(self):
        super(WFSocialCreativeCarouselSlideshowBlock, self).__init__(self.template_name)

        self._add_required_parameters([
            'Social Creative Message',
            'Social Advertiser Website URL',
            'Social Carousel/Slideshow',
            'Social Carousel S3 URI 1',
            'Social S3 Type 1',
            'Social Carousel Title 1',
            'Social Carousel Description 1',
            'Social Carousel URL 1',
            'Social Carousel S3 URI 2',
            'Social S3 Type 2',
            'Social Carousel Title 2',
            'Social Carousel Description 2',
            'Social Carousel URL 2',
            'Social Carousel S3 URI 3',
            'Social S3 Type 3',
            'Social Carousel Title 3',
            'Social Carousel Description 3',
            'Social Carousel URL 3',
            'FB/Instagram Call to Action',
            'FB/Instagram Facebook Platforms',
            'FB/Instagram Instagram Platforms',
        ])
        self._add_optional_parameters([
            'Social Carousel S3 URI 4',
            'Social S3 Type 4',
            'Social Carousel Title 4',
            'Social Carousel Description 4',
            'Social Carousel URL 4',
            'Social Carousel S3 URI 5',
            'Social S3 Type 5',
            'Social Carousel Title 5',
            'Social Carousel Description 5',
            'Social Carousel URL 5',
            'FB/Instagram Facebook Page ID',
            'FB/Instagram Instagram Account ID',
            'FB/Instagram Audience Network Platforms',
            'FB/Instagram Messenger Platforms',
        ])

        self._creatives = []
        self._message = None
        self._advertiser_website_url = None
        self._carousel_or_slideshow = None
        self._fb_call_to_action = None
        self._fb_facebook_platforms = None
        self._fb_instagram_platforms = None
        self._fb_facebook_page_id = None
        self._fb_instagram_account_id = None
        self._fb_audience_network_platforms = None
        self._fb_instagram_messenger_platforms = None

    def add_creative(self, **kwargs):
        n_creatives = len(self._creatives)
        if n_creatives == self.max_creatives:
            raise WFBrigeException('The maximum number of creatives for a Carousel or Slideshow is {}'
                                   .format(n_creatives))
        creative = {
            's3_uri': kwargs['s3_uri'],
            'asset_type': kwargs['asset_type'],
            'title': kwargs['title'],
            'description': kwargs['description'],
            'website_url': kwargs['website_url'],
        }
        self.set_parameter(self.create_carousel_slideshow_task_name,
                           'Social Carousel S3 URI {}'.format(n_creatives + 1), kwargs['s3_uri'])
        self.set_parameter(self.create_carousel_slideshow_task_name,
                           'Social S3 Type {}'.format(n_creatives + 1), kwargs['asset_type'])
        self.set_parameter(self.create_carousel_slideshow_task_name,
                           'Social Carousel Title {}'.format(n_creatives + 1), kwargs['title'])
        self.set_parameter(self.create_carousel_slideshow_task_name,
                           'Social Carousel Description {}'.format(n_creatives + 1), kwargs['description'])
        self.set_parameter(self.create_carousel_slideshow_task_name,
                           'Social Carousel URL {}'.format(n_creatives + 1), kwargs['website_url'])
        self._creatives.append(creative)

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, v):
        self._message = v
        self.set_parameter(self.create_carousel_slideshow_task_name, 'Social Creative Message', v)

    @property
    def advertiser_website_url(self):
        return self._advertiser_website_url

    @advertiser_website_url.setter
    def advertiser_website_url(self, v):
        self._advertiser_website_url = v
        self.set_parameter(self.create_carousel_slideshow_task_name, 'Social Advertiser Website URL', v)

    @property
    def fb_call_to_action(self):
        return self._fb_call_to_action

    @fb_call_to_action.setter
    def fb_call_to_action(self, v):
        self._fb_call_to_action = v
        self.set_parameter(self.create_carousel_slideshow_task_name, 'FB/Instagram Call to Action', v)

    @property
    def fb_facebook_platforms(self):
        return self._fb_facebook_platforms

    @fb_facebook_platforms.setter
    def fb_facebook_platforms(self, v):
        self._fb_facebook_platforms = v
        self.set_parameter(self.create_carousel_slideshow_task_name, 'FB/Instagram Facebook Platforms', v)

    @property
    def fb_instagram_platforms(self):
        return self._fb_instagram_platforms

    @fb_instagram_platforms.setter
    def fb_instagram_platforms(self, v):
        self._fb_instagram_platforms = v
        self.set_parameter(self.create_carousel_slideshow_task_name, 'FB/Instagram Instagram Platforms', v)

    @property
    def fb_facebook_page_id(self):
        return self._fb_facebook_page_id

    @fb_facebook_page_id.setter
    def fb_facebook_page_id(self, v):
        self._fb_facebook_page_id = v
        self.set_parameter(self.create_carousel_slideshow_task_name, 'FB/Instagram Facebook Page ID', v)

    @property
    def fb_instagram_account_id(self):
        return self._fb_instagram_account_id

    @fb_instagram_account_id.setter
    def fb_instagram_account_id(self, v):
        self._fb_instagram_account_id = v
        self.set_parameter(self.create_carousel_slideshow_task_name, 'FB/Instagram Instagram Account ID', v)

    @property
    def fb_audience_network_platforms(self):
        return self._fb_audience_network_platforms

    @fb_audience_network_platforms.setter
    def fb_audience_network_platforms(self, v):
        self._fb_audience_network_platforms = v
        self.set_parameter(self.create_carousel_slideshow_task_name, 'FB/Instagram Audience Network Platforms', v)

    @property
    def fb_instagram_messenger_platforms(self):
        return self._fb_instagram_messenger_platforms

    @fb_instagram_messenger_platforms.setter
    def fb_instagram_messenger_platforms(self, v):
        self._fb_instagram_messenger_platforms = v
        self.set_parameter(self.create_carousel_slideshow_task_name, 'FB/Instagram Messenger Platforms', v)
