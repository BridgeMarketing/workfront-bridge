from workfront_bridge.blocks.base import WFBlock


class WFAudioCreativeQABlock(WFBlock):
    """
    @summary: Audio QA Creative block
    """

    template_name = 'Block - Audio QA Creative'
    creative_qa_task_name = 'Creative QA'

    def __init__(self):
        super(WFAudioCreativeQABlock, self).__init__(self.template_name)
        self._add_required_parameters([
            "Creative Name",
            "AudioS3URL",
            "ThirdPartyImpressionTrackingUrl",
            "Duration",
        ])
        self._add_optional_parameters([
        ])
        self._creative_name = None
        self._audio_s3_url = None
        self._duration = None
        self._third_party_impression_tracking_url = None

    @property
    def creative_name(self):
        return self._creative_name

    @creative_name.setter
    def creative_name(self, v):
        self._creative_name = v
        self.set_parameter(self.creative_qa_task_name, "Creative Name", v)

    @property
    def audio_s3_url(self):
        return self._audio_s3_url

    @audio_s3_url.setter
    def audio_s3_url(self, v):
        self._audio_s3_url = v
        self.set_parameter(self.creative_qa_task_name, "AudioS3URL", v)

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, v):
        self._duration = v
        self.set_parameter(self.creative_qa_task_name, "Duration", v)

    @property
    def third_party_impression_tracking_url(self):
        return self._third_party_impression_tracking_url

    @third_party_impression_tracking_url.setter
    def third_party_impression_tracking_url(self, v):
        self._third_party_impression_tracking_url = v
        self.set_parameter(self.creative_qa_task_name, "ThirdPartyImpressionTrackingUrl", v)

