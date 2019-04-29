from workfront_bridge.blocks.base import WFBlock


class WFDisplayCreativeUploadBlock(WFBlock):
    """
    @summary: Display Creative Upload block
    """

    template_name = 'Block - Display Creative Upload v2'

    block_params = {
        'Creative Upload': [
            ('DisplayCreativeType', 'creative_type', True),
            ('Creative Name', 'creative_name', True),
            ('LandingPageUrl', 'landing_page_url', True),
            ('ClickthroughUrl', 'clickthrough_url', False),
            ('ImageS3URL', 'image_s3_url', False),
            ('ThirdPartyTags', 'third_party_tags', False),
            ('ThirdPartyImpressionTrackingUrl', 'third_party_impression_tracking_url', False),
            ('ThirdPartyImpressionTrackingUrl2', 'third_party_impression_tracking_url2', False),
            ('ThirdPartyImpressionTrackingUrl3', 'third_party_impression_tracking_url3', False),
            ('Securable', 'securable', False),
            ('Availability', 'availability', False),
            ('ThirdPartyTag', 'third_party_tag', False),
            ('Width', 'width', False),
            ('Height', 'height', False),
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
            ('NativeImageAssetIcon', 'native_image_asset_icon', False),
            ('NativeDecimalAssetRating', 'native_decimal_asset_rating', False),
            ('NativeTextAssetPrice', 'native_text_asset_price', False),
        ],
    }
