from workfront_bridge.blocks.base import WFBlock


class WFDisplayCreativeQABlock(WFBlock):
    """
    @summary: Display QA Creative block
    """

    template_name = 'Block - Display QA Creative'
    creative_qa_task_name = 'Creative QA'

    def __init__(self):
        super(WFDisplayCreativeQABlock, self).__init__(self.template_name)
        self._add_required_parameters([
            "Creative Name",
            "ImageS3URL",
            "Creative Size",
            "ClickthroughUrl",
            "LandingPageUrl",
        ])
        self._add_optional_parameters([
            "ThirdPartyTags",
            "ThirdPartyImpressionTrackingUrl",
        ])
        self._creative_name = None
        self._image_s3_url = None
        self._creative_size = None
        self._clickthrough_url = None
        self._landing_page_url = None
        self._third_party_tags = None
        self._third_party_impression_tracking_url = None

    @property
    def creative_name(self):
        return self._creative_name

    @creative_name.setter
    def creative_name(self, v):
        self._creative_name = v
        self.set_parameter(self.creative_qa_task_name, "Creative Name", v)

    @property
    def image_s3_url(self):
        return self._image_s3_url

    @image_s3_url.setter
    def image_s3_url(self, v):
        self._image_s3_url = v
        self.set_parameter(self.creative_qa_task_name, "ImageS3URL", v)

    @property
    def creative_size(self):
        return self._creative_size

    @creative_size.setter
    def creative_size(self, v):
        self._creative_size = v
        self.set_parameter(self.creative_qa_task_name, "Creative Size", v)

    @property
    def clickthrough_url(self):
        return self._clickthrough_url

    @clickthrough_url.setter
    def clickthrough_url(self, v):
        self._clickthrough_url = v
        self.set_parameter(self.creative_qa_task_name, "ClickthroughUrl", v)

    @property
    def landing_page_url(self):
        return self._landing_page_url

    @landing_page_url.setter
    def landing_page_url(self, v):
        self._landing_page_url = v
        self.set_parameter(self.creative_qa_task_name, "LandingPageUrl", v)

    @property
    def third_party_tags(self):
        return self._third_party_tags

    @third_party_tags.setter
    def third_party_tags(self, v):
        self._third_party_tags = v
        self.set_parameter(self.creative_qa_task_name, "ThirdPartyTags", v)

    @property
    def third_party_impression_tracking_url(self):
        return self._third_party_impression_tracking_url

    @third_party_impression_tracking_url.setter
    def third_party_impression_tracking_url(self, v):
        self._third_party_impression_tracking_url = v
        self.set_parameter(self.creative_qa_task_name, "ThirdPartyImpressionTrackingUrl", v)
