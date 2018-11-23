from workfront_bridge.blocks.base import WFBlock


class WFDisplayCreativeUploadBlock(WFBlock):
    """
    @summary: Display Creative Upload block
    """

    template_name = 'Block - Display Creative Upload v2'
    creative_upload_task_name = 'Creative Upload'

    def __init__(self):
        super(WFDisplayCreativeUploadBlock, self).__init__(self.template_name)
        self._add_required_parameters([
            "DisplayCreativeType",
            "CreativeName",
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
            # Native
            "NativeTextAssetTitle",
            "NativeTextAssetSponsor",
            "NativeTextAssetDescription",
            "NativeTextAssetCallToAction",
            "NativeTextAssetOptOutUrl",
            "NativeTextAssetOptOutText",
            "NativeImageAssetMain",
            "NativeImageAssetLogo",
            "NativeImageAssetIcon",
            "NativeDecimalAssetRating",
            "NativeDecimalAssetPrice",
        ])
        self._creative_type = None
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

        # Native
        self._native_text_asset_title = None
        self._native_text_asset_sponsor = None
        self._native_text_asset_description = None
        self._native_text_asset_call_to_action = None
        self._native_text_asset_opt_out_url = None
        self._native_text_asset_opt_out_text = None
        self._native_image_asset_main = None
        self._native_image_asset_logo = None
        self._native_image_asset_icon = None
        self._native_decimal_asset_rating = None
        self._native_decimal_asset_price = None

    @property
    def creative_type(self):
        return self._creative_type

    @creative_type.setter
    def creative_type(self, v):
        self._creative_type = v
        self.set_parameter(self.creative_upload_task_name, "DisplayCreativeType", v)

    @property
    def creative_name(self):
        return self._creative_name

    @creative_name.setter
    def creative_name(self, v):
        self._creative_name = v
        self.set_parameter(self.creative_upload_task_name, "CreativeName", v)

    @property
    def image_s3_url(self):
        return self._image_s3_url

    @image_s3_url.setter
    def image_s3_url(self, v):
        self._image_s3_url = v
        self.set_parameter(self.creative_upload_task_name, "ImageS3URL", v)

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
    def third_party_tags(self):
        return self._third_party_tags

    @third_party_tags.setter
    def third_party_tags(self, v):
        self._third_party_tags = v
        self.set_parameter(self.creative_upload_task_name, "ThirdPartyTags", v)

    @property
    def third_party_impression_tracking_url(self):
        return self._third_party_impression_tracking_url

    @third_party_impression_tracking_url.setter
    def third_party_impression_tracking_url(self, v):
        self._third_party_impression_tracking_url = v
        self.set_parameter(self.creative_upload_task_name, "ThirdPartyImpressionTrackingUrl", v)

    @property
    def third_party_impression_tracking_url2(self):
        return self._third_party_impression_tracking_url2

    @third_party_impression_tracking_url2.setter
    def third_party_impression_tracking_url2(self, v):
        self._third_party_impression_tracking_url2 = v
        self.set_parameter(self.creative_upload_task_name, "ThirdPartyImpressionTrackingUrl2", v)

    @property
    def third_party_impression_tracking_url3(self):
        return self._third_party_impression_tracking_url3

    @third_party_impression_tracking_url3.setter
    def third_party_impression_tracking_url3(self, v):
        self._third_party_impression_tracking_url3 = v
        self.set_parameter(self.creative_upload_task_name, "ThirdPartyImpressionTrackingUrl3", v)

    @property
    def securable(self):
        return self._securable

    @securable.setter
    def securable(self, v):
        self._securable = v
        self.set_parameter(self.creative_upload_task_name, "Securable", v)

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, v):
        self._availability = v
        self.set_parameter(self.creative_upload_task_name, "Availability", v)

    @property
    def third_party_tag(self):
        return self._third_party_tag

    @third_party_tag.setter
    def third_party_tag(self, v):
        self._third_party_tag = v
        self.set_parameter(self.creative_upload_task_name, "ThirdPartyTag", v)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, v):
        self._width = v
        self.set_parameter(self.creative_upload_task_name, "Width", v)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, v):
        self._height = v
        self.set_parameter(self.creative_upload_task_name, "Height", v)

    @property
    def native_text_asset_title(self):
        return self._native_text_asset_title

    @native_text_asset_title.setter
    def native_text_asset_title(self, v):
        self._native_text_asset_title = v
        self.set_parameter(self.creative_upload_task_name, "NativeTextAssetTitle", v)

    @property
    def native_text_asset_sponsor(self):
        return self._native_text_asset_sponsor

    @native_text_asset_sponsor.setter
    def native_text_asset_sponsor(self, v):
        self._native_text_asset_sponsor = v
        self.set_parameter(self.creative_upload_task_name, "NativeTextAssetSponsor", v)

    @property
    def native_text_asset_description(self):
        return self._native_text_asset_description

    @native_text_asset_description.setter
    def native_text_asset_description(self, v):
        self._native_text_asset_description = v
        self.set_parameter(self.creative_upload_task_name, "NativeTextAssetDescription", v)

    @property
    def native_text_asset_call_to_action(self):
        return self._native_text_asset_call_to_action

    @native_text_asset_call_to_action.setter
    def native_text_asset_call_to_action(self, v):
        self._native_text_asset_call_to_action = v
        self.set_parameter(self.creative_upload_task_name, "NativeTextAssetCallToAction", v)

    @property
    def native_text_asset_opt_out_url(self):
        return self._native_text_asset_opt_out_url

    @native_text_asset_opt_out_url.setter
    def native_text_asset_opt_out_url(self, v):
        self._native_text_asset_opt_out_url = v
        self.set_parameter(self.creative_upload_task_name, "NativeTextAssetOptOutUrl", v)

    @property
    def native_text_asset_opt_out_text(self):
        return self._native_text_asset_opt_out_text

    @native_text_asset_opt_out_text.setter
    def native_text_asset_opt_out_text(self, v):
        self._native_text_asset_opt_out_text = v
        self.set_parameter(self.creative_upload_task_name, "NativeTextAssetOptOutText", v)

    @property
    def native_image_asset_main(self):
        return self._native_image_asset_main

    @native_image_asset_main.setter
    def native_image_asset_main(self, v):
        self._native_image_asset_main = v
        self.set_parameter(self.creative_upload_task_name, "NativeImageAssetMain", v)

    @property
    def native_image_asset_logo(self):
        return self._native_image_asset_logo

    @native_image_asset_logo.setter
    def native_image_asset_logo(self, v):
        self._native_image_asset_logo = v
        self.set_parameter(self.creative_upload_task_name, "NativeImageAssetLogo", v)

    @property
    def native_image_asset_icon(self):
        return self._native_image_asset_icon

    @native_image_asset_icon.setter
    def native_image_asset_icon(self, v):
        self._native_image_asset_icon = v
        self.set_parameter(self.creative_upload_task_name, "NativeImageAssetIcon", v)

    @property
    def native_decimal_asset_rating(self):
        return self._native_decimal_asset_rating

    @native_decimal_asset_rating.setter
    def native_decimal_asset_rating(self, v):
        self._native_decimal_asset_rating = v
        self.set_parameter(self.creative_upload_task_name, "NativeDecimalAssetRating", v)

    @property
    def native_decimal_asset_price(self):
        return self._native_decimal_asset_price

    @native_decimal_asset_price.setter
    def native_decimal_asset_price(self, v):
        self._native_decimal_asset_price = v
        self.set_parameter(self.creative_upload_task_name, "NativeDecimalAssetPrice", v)
