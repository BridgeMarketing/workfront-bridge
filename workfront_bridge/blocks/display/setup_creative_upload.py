from workfront_bridge.blocks.base import WFBlock


class WFDisplayCreativeUploadBlock(WFBlock):
    """
    @summary: Display Creative Upload block
    """

    template_name = 'Block - Display Creative Upload'

    def __init__(self):
        super(WFDisplayCreativeUploadBlock, self).__init__(self.template_name)
        self._add_required_parameters([
            "Creative Name",
            "LandingPageUrl",
        ])
        self._add_optional_parameters([
            "ClickthroughUrl",
            "ImageS3URL",
            "ThirdPartyTags",
            "ThirdPartyImpressionTrackingUrl",
            "ThirdPartyImpressionTrackingUrl2",
            "ThirdPartyImpressionTrackingUrl3",
            "Securable",
            "Availability",
            "ThirdPartyTag",
            "Width",
            "Height",
        ])
        self._creative_name = None
        self._image_s3_url = None
        self._clickthrough_url = None
        self._landing_page_url = None
        self._third_party_tags = None
        self._third_party_impression_tracking_url = None
        self._third_party_impression_tracking_url2 = None
        self._third_party_impression_tracking_url3 = None
        self._securable = None
        self._availability = None
        self._third_party_tag = None
        self._width = None
        self._height = None

    @property
    def creative_name(self):
        return self._creative_name

    @creative_name.setter
    def creative_name(self, v):
        self._creative_name = v
        self.set_parameter("Creative Upload", "Creative Name", v)

    @property
    def image_s3_url(self):
        return self._image_s3_url

    @image_s3_url.setter
    def image_s3_url(self, v):
        self._image_s3_url = v
        self.set_parameter("Creative Upload", "ImageS3URL", v)

    @property
    def clickthrough_url(self):
        return self._clickthrough_url

    @clickthrough_url.setter
    def clickthrough_url(self, v):
        self._clickthrough_url = v
        self.set_parameter("Creative Upload", "ClickthroughUrl", v)

    @property
    def landing_page_url(self):
        return self._landing_page_url

    @landing_page_url.setter
    def landing_page_url(self, v):
        self._landing_page_url = v
        self.set_parameter("Creative Upload", "LandingPageUrl", v)

    @property
    def third_party_tags(self):
        return self._third_party_tags

    @third_party_tags.setter
    def third_party_tags(self, v):
        self._third_party_tags = v
        self.set_parameter("Creative Upload", "ThirdPartyTags", v)

    @property
    def third_party_impression_tracking_url(self):
        return self._third_party_impression_tracking_url

    @third_party_impression_tracking_url.setter
    def third_party_impression_tracking_url(self, v):
        self._third_party_impression_tracking_url = v
        self.set_parameter("Creative Upload", "ThirdPartyImpressionTrackingUrl", v)

    @property
    def third_party_impression_tracking_url2(self):
        return self._third_party_impression_tracking_url2

    @third_party_impression_tracking_url2.setter
    def third_party_impression_tracking_url2(self, v):
        self._third_party_impression_tracking_url2 = v
        self.set_parameter("Creative Upload", "ThirdPartyImpressionTrackingUrl2", v)

    @property
    def third_party_impression_tracking_url3(self):
        return self._third_party_impression_tracking_url3

    @third_party_impression_tracking_url3.setter
    def third_party_impression_tracking_url3(self, v):
        self._third_party_impression_tracking_url3 = v
        self.set_parameter("Creative Upload", "ThirdPartyImpressionTrackingUrl3", v)

    @property
    def securable(self):
        return self._securable

    @securable.setter
    def securable(self, v):
        self._securable = v
        self.set_parameter("Creative Upload", "Securable", v)

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, v):
        self._availability = v
        self.set_parameter("Creative Upload", "Availability", v)

    @property
    def third_party_tag(self):
        return self._third_party_tag

    @third_party_tag.setter
    def third_party_tag(self, v):
        self._third_party_tag = v
        self.set_parameter("Creative Upload", "ThirdPartyTag", v)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, v):
        self._width = v
        self.set_parameter("Creative Upload", "Width", v)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, v):
        self._height = v
        self.set_parameter("Creative Upload", "Height", v)
