from workfront_bridge.blocks.base import WFBlock


class WFAudioCreativeUploadBlock(WFBlock):
    """
    @summary: Audio Creative Upload block
    """

    template_name = 'Block - Audio Creative Upload'
    creative_upload_task_name = 'Creative Upload'

    def __init__(self):
        super(WFAudioCreativeUploadBlock, self).__init__(self.template_name)
        self._add_required_parameters([
            "Creative Name",
            "LandingPageUrl",
            "ClickthroughUrl",
            "type",
        ])
        self._add_optional_parameters([
            "ClickthroughUrl",
            "AudioS3URL",
            "ThirdPartyImpressionTrackingUrl",
            "Duration",
            "Height",
        ])
        self._creative_name = None
        self._audio_s3_url = None
        self._third_party_impression_tracking_url = None
        self._duration = None
        self._clickthrough_url = None
        self._landing_page_url = None

        self.automation_type = ' AudioCreativeUpload'

    @property
    def automation_type(self):
        return self._automation_type

    @automation_type.setter
    def automation_type(self, v):
        self._automation_type = v
        self.set_parameter(self.creative_upload_task_name, "type", v)

    @property
    def creative_name(self):
        return self._creative_name

    @creative_name.setter
    def creative_name(self, v):
        self._creative_name = v
        self.set_parameter(self.creative_upload_task_name, "Creative Name", v)

    @property
    def audio_s3_url(self):
        return self._audio_s3_url

    @audio_s3_url.setter
    def audio_s3_url(self, v):
        self._audio_s3_url = v
        self.set_parameter(self.creative_upload_task_name, "AudioS3URL", v)

    @property
    def third_party_impression_tracking_url(self):
        return self._third_party_impression_tracking_url

    @third_party_impression_tracking_url.setter
    def third_party_impression_tracking_url(self, v):
        self._third_party_impression_tracking_url = v
        self.set_parameter(self.creative_upload_task_name, "ThirdPartyImpressionTrackingUrl", v)

    @property
    def clickthrough_url(self):
        return self._clickthrough_url

    @clickthrough_url.setter
    def clickthrough_url(self, v):
        self._clickthrough_url = v
        self.set_parameter(self.creative_upload_task_name, "ClickthroughUrl", v)

    @property
    def landing_page_url(self):
        return self._landing_page_url

    @landing_page_url.setter
    def landing_page_url(self, v):
        self._landing_page_url = v
        self.set_parameter(self.creative_upload_task_name, "LandingPageUrl", v)

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, v):
        self._duration = v
        self.set_parameter(self.creative_upload_task_name, "Duration", v)
