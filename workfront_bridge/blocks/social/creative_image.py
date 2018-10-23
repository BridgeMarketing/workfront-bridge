from workfront_bridge.blocks.base import WFBlock


class WFSocialCreativeImageBlock(WFBlock):
    """
    @summary: Social Creative Image block
    """

    template_name = 'Block - Social Image'
    create_image_task_name = 'Create Creative Image'

    def __init__(self):
        super(WFSocialCreativeImageBlock, self).__init__(self.template_name)

        self._add_required_parameters([
            'Social Creative Message',
            'Social Advertiser Website URL',
            'Social Image S3 URI',
            'Social Title',
            'Social Description',
            'FB/Instagram Call to Action',
            'FB/Instagram Facebook Platforms',
            'FB/Instagram Instagram Platforms',
        ])
        self._add_optional_parameters([
            'FB/Instagram Facebook Page ID',
            'FB/Instagram Instagram Account ID',
            'FB/Instagram Audience Network Platforms',
            'FB/Instagram Messenger Platforms',
        ])

        self._message = None
        self._advertiser_website_url = None
        self._s3_uri = None
        self._title = None
        self._description = None
        self._fb_call_to_action = None
        self._fb_facebook_platforms = None
        self._fb_instagram_platforms = None
        self._fb_facebook_page_id = None
        self._fb_instagram_account_id = None
        self._fb_audience_network_platforms = None
        self._fb_instagram_messenger_platforms = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, v):
        self._message = v
        self.set_parameter(self.create_image_task_name, 'Social Creative Message', v)

    @property
    def advertiser_website_url(self):
        return self._advertiser_website_url

    @advertiser_website_url.setter
    def advertiser_website_url(self, v):
        self._advertiser_website_url = v
        self.set_parameter(self.create_image_task_name, 'Social Advertiser Website URL', v)

    @property
    def s3_uri(self):
        return self._s3_uri

    @s3_uri.setter
    def s3_uri(self, v):
        self._s3_uri = v
        self.set_parameter(self.create_image_task_name, 'Social Image S3 URI', v)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, v):
        self._title = v
        self.set_parameter(self.create_image_task_name, 'Social Title', v)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, v):
        self._description = v
        self.set_parameter(self.create_image_task_name, 'Social Description', v)

    @property
    def fb_call_to_action(self):
        return self._fb_call_to_action

    @fb_call_to_action.setter
    def fb_call_to_action(self, v):
        self._fb_call_to_action = v
        self.set_parameter(self.create_image_task_name, 'FB/Instagram Call to Action', v)

    @property
    def fb_facebook_platforms(self):
        return self._fb_facebook_platforms

    @fb_facebook_platforms.setter
    def fb_facebook_platforms(self, v):
        self._fb_facebook_platforms = v
        self.set_parameter(self.create_image_task_name, 'FB/Instagram Facebook Platforms', v)

    @property
    def fb_instagram_platforms(self):
        return self._fb_instagram_platforms

    @fb_instagram_platforms.setter
    def fb_instagram_platforms(self, v):
        self._fb_instagram_platforms = v
        self.set_parameter(self.create_image_task_name, 'FB/Instagram Instagram Platforms', v)

    @property
    def fb_facebook_page_id(self):
        return self._fb_facebook_page_id

    @fb_facebook_page_id.setter
    def fb_facebook_page_id(self, v):
        self._fb_facebook_page_id = v
        self.set_parameter(self.create_image_task_name, 'FB/Instagram Facebook Page ID', v)

    @property
    def fb_instagram_account_id(self):
        return self._fb_instagram_account_id

    @fb_instagram_account_id.setter
    def fb_instagram_account_id(self, v):
        self._fb_instagram_account_id = v
        self.set_parameter(self.create_image_task_name, 'FB/Instagram Instagram Account ID', v)

    @property
    def fb_audience_network_platforms(self):
        return self._fb_audience_network_platforms

    @fb_audience_network_platforms.setter
    def fb_audience_network_platforms(self, v):
        self._fb_audience_network_platforms = v
        self.set_parameter(self.create_image_task_name, 'FB/Instagram Audience Network Platforms', v)

    @property
    def fb_instagram_messenger_platforms(self):
        return self._fb_instagram_messenger_platforms

    @fb_instagram_messenger_platforms.setter
    def fb_instagram_messenger_platforms(self, v):
        self._fb_instagram_messenger_platforms = v
        self.set_parameter(self.create_image_task_name, 'FB/Instagram Messenger Platforms', v)
