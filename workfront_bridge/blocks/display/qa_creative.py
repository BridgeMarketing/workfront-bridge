from workfront_bridge.blocks.base import WFBlock


class WFDisplayCreativeQABlock(WFBlock):
    """
    @summary: Display QA Creative block
    """

    template_name = 'Block - Display QA Creative v2'

    block_params = {
        'Creative QA': [
            ('Creative Name', 'creative_name', True),
            ('ClickthroughUrl', 'clickthrough_url', True),
            ('LandingPageUrl', 'landing_page_url', True),
            ('ImageS3URL', 'image_s3_url', False),
            ('Creative Size', 'creative_size', False),
            ('ThirdPartyTags', 'third_party_tags', False),
            ('ThirdPartyImpressionTrackingUrl', 'third_party_impression_tracking_url', False),
            ('NativeTextAssetTitleLong', 'native_text_asset_title_long', False),
            ('NativeTextAssetTitleShort', 'native_text_asset_title_short', False),
            ('NativeTextAssetSponsor', 'native_text_asset_sponsor', False),
            ('NativeTextAssetDescriptionLong', 'native_text_asset_description_long', False),
            ('NativeTextAssetDescriptionShort', 'native_text_asset_description_short', False),
            ('NativeTextAssetCallToAction', 'native_text_asset_call_to_action', False),
            ('NativeTextAssetOptOutUrl', 'native_text_asset_opt_out_url', False),
            ('NativeTextAssetOptOutText', 'native_text_asset_opt_out_text', False),
            ('NativeImageAssetMain', 'native_image_asset_main', False),
            ('NativeImageAssetLogo', 'native_image_asset_logo', False),
            ('NativeDecimalAssetRating', 'native_decimal_asset_rating', False),
            ('NativeTextAssetPrice', 'native_text_asset_price', False),
        ],
    }
