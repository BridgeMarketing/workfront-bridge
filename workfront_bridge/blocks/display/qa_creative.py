from workfront_bridge.blocks.base import WFBlock


class WFDisplayCreativeQABlock(WFBlock):
    """
    @summary: Display QA Creative block
    """

    template_name = 'Block - Display QA Creative v2'
    creative_qa_task_name = 'Creative QA'

    def __init__(self):
        super(WFDisplayCreativeQABlock, self).__init__(self.template_name)
        self._add_required_parameters([
            "Creative Name",
            "ClickthroughUrl",
            "LandingPageUrl",
        ])
        self._add_optional_parameters([
            "ImageS3URL",
            "Creative Size",
            "ThirdPartyTags",
            "ThirdPartyImpressionTrackingUrl",
            # Native
            "NativeTextAssetTitleLong",
            "NativeTextAssetTitleShort",
            "NativeTextAssetSponsor",
            "NativeTextAssetDescriptionLong",
            "NativeTextAssetDescriptionShort",
            "NativeTextAssetCallToAction",
            "NativeTextAssetOptOutUrl",
            "NativeTextAssetOptOutText",
            "NativeImageAssetMain",
            "NativeImageAssetLogo",
            "NativeImageAssetIcon",
            "NativeDecimalAssetRating",
            "NativeTextAssetPrice",
        ])
        self._creative_name = None
        self._image_s3_url = None
        self._creative_size = None
        self._clickthrough_url = None
        self._landing_page_url = None
        self._third_party_tags = None
        self._third_party_impression_tracking_url = None

        # Native
        self._native_text_asset_title_long = None
        self._native_text_asset_title_short = None
        self._native_text_asset_sponsor = None
        self._native_text_asset_description_long = None
        self._native_text_asset_description_short = None
        self._native_text_asset_call_to_action = None
        self._native_text_asset_opt_out_url = None
        self._native_text_asset_opt_out_text = None
        self._native_image_asset_main = None
        self._native_image_asset_logo = None
        self._native_image_asset_icon = None
        self._native_decimal_asset_rating = None
        self._native_text_asset_price = None

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

    @property
    def native_text_asset_title_long(self):
        return self._native_text_asset_title_long

    @native_text_asset_title_long.setter
    def native_text_asset_title_long(self, v):
        self._native_text_asset_title_long = v
        self.set_parameter(self.creative_qa_task_name, "NativeTextAssetTitleLong", v)

    @property
    def native_text_asset_title_short(self):
        return self._native_text_asset_title_short

    @native_text_asset_title_short.setter
    def native_text_asset_title_short(self, v):
        self._native_text_asset_title_short = v
        self.set_parameter(self.creative_qa_task_name, "NativeTextAssetTitleShort", v)

    @property
    def native_text_asset_sponsor(self):
        return self._native_text_asset_sponsor

    @native_text_asset_sponsor.setter
    def native_text_asset_sponsor(self, v):
        self._native_text_asset_sponsor = v
        self.set_parameter(self.creative_qa_task_name, "NativeTextAssetSponsor", v)

    @property
    def native_text_asset_description_long(self):
        return self._native_text_asset_description_long

    @native_text_asset_description_long.setter
    def native_text_asset_description_long(self, v):
        self._native_text_asset_description_long = v
        self.set_parameter(self.creative_qa_task_name, "NativeTextAssetDescriptionLong", v)

    @property
    def native_text_asset_description_short(self):
        return self._native_text_asset_description_short

    @native_text_asset_description_short.setter
    def native_text_asset_description_short(self, v):
        self._native_text_asset_description_short = v
        self.set_parameter(self.creative_qa_task_name, "NativeTextAssetDescriptionShort", v)

    @property
    def native_text_asset_call_to_action(self):
        return self._native_text_asset_call_to_action

    @native_text_asset_call_to_action.setter
    def native_text_asset_call_to_action(self, v):
        self._native_text_asset_call_to_action = v
        self.set_parameter(self.creative_qa_task_name, "NativeTextAssetCallToAction", v)

    @property
    def native_text_asset_opt_out_url(self):
        return self._native_text_asset_opt_out_url

    @native_text_asset_opt_out_url.setter
    def native_text_asset_opt_out_url(self, v):
        self._native_text_asset_opt_out_url = v
        self.set_parameter(self.creative_qa_task_name, "NativeTextAssetOptOutUrl", v)

    @property
    def native_text_asset_opt_out_text(self):
        return self._native_text_asset_opt_out_text

    @native_text_asset_opt_out_text.setter
    def native_text_asset_opt_out_text(self, v):
        self._native_text_asset_opt_out_text = v
        self.set_parameter(self.creative_qa_task_name, "NativeTextAssetOptOutText", v)

    @property
    def native_image_asset_main(self):
        return self._native_image_asset_main

    @native_image_asset_main.setter
    def native_image_asset_main(self, v):
        self._native_image_asset_main = v
        self.set_parameter(self.creative_qa_task_name, "NativeImageAssetMain", v)

    @property
    def native_image_asset_logo(self):
        return self._native_image_asset_logo

    @native_image_asset_logo.setter
    def native_image_asset_logo(self, v):
        self._native_image_asset_logo = v
        self.set_parameter(self.creative_qa_task_name, "NativeImageAssetLogo", v)

    @property
    def native_image_asset_icon(self):
        return self._native_image_asset_icon

    @native_image_asset_icon.setter
    def native_image_asset_icon(self, v):
        self._native_image_asset_icon = v
        self.set_parameter(self.creative_qa_task_name, "NativeImageAssetIcon", v)

    @property
    def native_decimal_asset_rating(self):
        return self._native_decimal_asset_rating

    @native_decimal_asset_rating.setter
    def native_decimal_asset_rating(self, v):
        self._native_decimal_asset_rating = v
        self.set_parameter(self.creative_qa_task_name, "NativeDecimalAssetRating", v)

    @property
    def native_text_asset_price(self):
        return self._native_text_asset_price

    @native_text_asset_price.setter
    def native_text_asset_price(self, v):
        self._native_text_asset_price = v
        self.set_parameter(self.creative_qa_task_name, "NativeTextAssetPrice", v)
