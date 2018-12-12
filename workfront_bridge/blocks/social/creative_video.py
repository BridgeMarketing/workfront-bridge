from workfront_bridge.blocks.base import WFBlock


class WFSocialCreativeVideoBlock(WFBlock):
    """
    @summary: Social Creative Video block
    """

    template_name = 'Block - Social Video'
    create_video_task_name = 'Create Creative Video'

    def __init__(self):
        super(WFSocialCreativeVideoBlock, self).__init__(self.template_name)

        self._add_required_parameters([
            'Social Creative Message',
            'Social Advertiser Website URL',
            'Social Video S3 URI',
            'Social Video Image S3 URI',
        ])
        self._add_optional_parameters([
            'type',
            'Social Title',
            'FB/Instagram Call to Action',
        ])

        self._message = None
        self._advertiser_website_url = None
        self._s3_uri = None
        self._image_s3_uri = None
        self._task_type = None
        self._title = None
        self._fb_call_to_action = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, v):
        self._message = v
        self.set_parameter(self.create_video_task_name, 'Social Creative Message', v)

    @property
    def advertiser_website_url(self):
        return self._advertiser_website_url

    @advertiser_website_url.setter
    def advertiser_website_url(self, v):
        self._advertiser_website_url = v
        self.set_parameter(self.create_video_task_name, 'Social Advertiser Website URL', v)

    @property
    def s3_uri(self):
        return self._s3_uri

    @s3_uri.setter
    def s3_uri(self, v):
        self._s3_uri = v
        self.set_parameter(self.create_video_task_name, 'Social Video S3 URI', v)

    @property
    def image_s3_uri(self):
        return self._image_s3_uri

    @image_s3_uri.setter
    def image_s3_uri(self, v):
        self._image_s3_uri = v
        self.set_parameter(self.create_video_task_name, 'Social Video Image S3 URI', v)

    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, v):
        self._task_type = v
        self.set_parameter(self.create_video_task_name, 'type', v)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, v):
        self._title = v
        self.set_parameter(self.create_video_task_name, 'Social Title', v)

    @property
    def fb_call_to_action(self):
        return self._fb_call_to_action

    @fb_call_to_action.setter
    def fb_call_to_action(self, v):
        self._fb_call_to_action = v
        self.set_parameter(self.create_video_task_name, 'FB/Instagram Call to Action', v)
