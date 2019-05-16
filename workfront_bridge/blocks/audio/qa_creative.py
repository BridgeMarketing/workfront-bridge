from workfront_bridge.blocks.base import WFBlock


class WFAudioCreativeQABlock(WFBlock):
    """
    @summary: Audio QA Creative block
    """

    template_name = 'Block - Media QA Creative'

    block_params = {
        'Creative QA': [
            ('Creative Name', 'creative_name', True),
            ('ClickthroughUrl', 'clickthrough_url', True),
            ('LandingPageUrl', 'landing_page_url', True),
            ('MediaS3URL', 'media_s3_url', False),
            ('ThirdPartyImpressionTrackingUrl', 'third_party_impression_tracking_url', False),
            ('Duration', 'duration', False),
        ],
    }
