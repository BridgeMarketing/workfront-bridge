from workfront_bridge.blocks.base import WFBlock


class WFAudioCreativeUploadBlock(WFBlock):
    """
    @summary: Audio Creative Upload block
    """

    template_name = 'Block - Audio Creative Upload'

    block_params = {
        'Creative Upload': [
            ('Creative Name', 'creative_name', True),
            ('LandingPageUrl', 'landing_page_url', True),
            ('ClickthroughUrl', 'clickthrough_url', True),
            ('type', 'automation_type', True),
            ('ClickthroughUrl', 'clickthrough_url', False),
            ('AudioS3URL', 'audio_s3_url', False),
            ('ThirdPartyImpressionTrackingUrl', 'third_party_impression_tracking_url', False),
            ('Duration', 'duration', False),
            ('Height', 'height', False),
        ],
    }

    def __init__(self):
        super(WFAudioCreativeUploadBlock, self).__init__(self.template_name)
        self.automation_type = 'AudioCreativeUpload'
