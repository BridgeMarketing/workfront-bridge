from workfront_bridge.projects.display import WFProjectDisplayContainer
from workfront_bridge.blocks.display.ad_group import WFDisplayAdGroupBlock
from workfront_bridge.blocks.display.campaign import WFDisplayCampaignBlock
from workfront_bridge.blocks.display.data import WFDisplayDataBlock
from workfront_bridge.blocks.display.launch import WFDisplayLaunchBlock
from workfront_bridge.blocks.display.order_review import WFDisplayOrderReviewBlock
from workfront_bridge.blocks.display.qa import WFDisplayQABlock
from workfront_bridge.blocks.display.setup import WFDisplaySetupBlock
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.blocks.base import WFBlockParser


class DisplayProjectBuilder(object):
    """
    @summary: Display project builder
    """
    creative_upload_params = [
        "creative_name",
        "image_s3_url",
        "clickthrough_url",
        "landing_page_url",
        "third_party_tags",
        "third_party_impression_tracking_url",
        "third_party_impression_tracking_url2",
        "third_party_impression_tracking_url3",
        "securable",
        "availability",
        "third_party_tag",
        "width",
        "height",
    ]
    creative_qa_params = [
        "creative_name",
        "image_s3_url",
        "creative_size",
        "clickthrough_url",
        "landing_page_url",
        "third_party_tags",
        "third_party_impression_tracking_url",
    ]

    def __init__(self, wf, project_name):
        """
        @param wf: Workfront service object
        @param project_name: project name in Workfront
        """
        self.project_name = project_name
        self.wf = wf
        self.creatives = []

        # project level
        self._ttd_audience_id = None
        self._ttd_campaign_id = None
        self._ttd_flight_id = None
        self._ttd_creative_id = None
        self._ttd_advertiser_id = None
        self._is_targeted_bonus_media = None
        self._project_type = None

        # data block
        self._audience_name = None

        # campaign block
        self._start_date_inclusive_utc = None
        self._end_date_exclusive_utc = None
        self._campaign_name = None
        self._campaign_overview = None
        self._partner_cost_percentage_fee = None
        self._availability = None
        self._auto_allocator = None
        self._ctv_targeting_and_attribution = None
        self._pacing_mode = None
        self._partner_cpm_fee_amount = None
        self._partner_cpm_fee_currency = None
        self._partner_cpc_fee_amount = None
        self._partner_cpc_fee_currency = None
        self._max_bid_amount = None
        self._budget_in_impressions_pre_calc = None
        self._daily_target_in_advertiser_currency = None
        self._daily_target_in_impressions = None

        # ad group block
        self._ad_group_name = None
        self._adg_base_bid_amount = None
        self._adg_description = None
        self._adg_daily_budget = None
        self._adg_daily_budget_in_impressions = None
        self._adg_budget_in_impressions_pre_calc = None
        self._adg_pacing_mode = None
        self._adg_auto_allocator_priority = None
        self._adg_max_bid_amount = None
        self._adg_frequency_period_in_minutes = None
        self._adg_frequency_cap = None
        self._adg_frequency_pricing_slope_cpm = None
        self._adg_ctr_in_percent = None
        self._device_type = None
        self._country = None
        self._category = None
        self._ae_excluder = None

    def add_creative(self, **kwargs):
        """Allowed kwargs:
        * creative_name - required
        * creative_size - required
        * image_s3_url - required
        * clickthrough_url - required
        * landing_page_url - required
        * third_party_tags
        * third_party_impression_tracking_url
        * third_party_impression_tracking_url2
        * third_party_impression_tracking_url3
        * securable
        * availability
        * third_party_tag
        * width
        * height
        """
        allowed_kwargs = set(DisplayProjectBuilder.creative_upload_params + DisplayProjectBuilder.creative_qa_params)
        creative = {}
        for k, v in kwargs.items():
            if k not in allowed_kwargs:
                raise WFBrigeException('Invalid Key {}'.format(k))
            creative[k] = v
        self.creatives.append(creative)

    def build(self):
        """
        @summary: build the Workfront project.
        @raise WFBrigeException
        @return: WFProject object
        """
        if not self.creatives:
            raise WFBrigeException('The project does not have any creatives. Please use add_creative to add them.')

        project = WFProjectDisplayContainer(self.project_name)

        order_review_block = WFDisplayOrderReviewBlock()    # Manual

        setup_block = WFDisplaySetupBlock()
        [setup_block.add_creative(
            **{k: creative[k] for k in DisplayProjectBuilder.creative_upload_params if k in creative}
        )
         for creative in self.creatives]

        ad_group_block = WFDisplayAdGroupBlock()
        ad_group_block.ad_group_name = self._ad_group_name
        ad_group_block.adg_base_bid_amount = self._adg_base_bid_amount

        campaign_block = WFDisplayCampaignBlock()
        campaign_block.start_date_inclusive_utc = self._start_date_inclusive_utc
        campaign_block.end_date_exclusive_utc = self._end_date_exclusive_utc
        campaign_block.campaign_name = self._campaign_name

        data_block = WFDisplayDataBlock()
        data_block.audience_name = self._audience_name

        qa_block = WFDisplayQABlock()   # Manual
        [qa_block.add_creative(
            **{k: creative[k] for k in DisplayProjectBuilder.creative_qa_params if k in creative}
        )
         for creative in self.creatives]

        qa_block.add_final_review(
            start_date_inclusive_utc=self._start_date_inclusive_utc,
            end_date_exclusive_utc=self._end_date_exclusive_utc,
            campaign_name=self._campaign_name,
            ad_group_name=self._ad_group_name,
            adg_base_bid_amount=self._adg_base_bid_amount,
        )

        launch_block = WFDisplayLaunchBlock()   # Manual

        [project.append(block) for block in [
            order_review_block,
            data_block,
            campaign_block,
            setup_block,
            ad_group_block,
            qa_block,
            launch_block,
        ]]
        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)
        return wf_project

    # Setters so Pablo doesn't go mad
    def set_ttd_audience_id(self, v):
        self._ttd_audience_id = v
        return self

    def set_ttd_campaign_id(self, v):
        self._ttd_campaign_id = v
        return self

    def set_ttd_flight_id(self, v):
        self._ttd_flight_id = v
        return self

    def set_ttd_creative_id(self, v):
        self._ttd_creative_id = v
        return self

    def set_ttd_advertiser_id(self, v):
        self._ttd_advertiser_id = v
        return self

    def set_is_targeted_bonus_media(self, v):
        self._is_targeted_bonus_media = v
        return self

    def set_project_type(self, v):
        self._project_type = v
        return self

    def set_audience_name(self, v):
        self._audience_name = v
        return self

    def set_start_date_inclusive_utc(self, v):
        self._start_date_inclusive_utc = v
        return self

    def set_end_date_exclusive_utc(self, v):
        self._end_date_exclusive_utc = v
        return self

    def set_campaign_name(self, v):
        self._campaign_name = v
        return self

    def set_campaign_overview(self, v):
        self._campaign_overview = v
        return self

    def set_partner_cost_percentage_fee(self, v):
        self._partner_cost_percentage_fee = v
        return self

    def set_availability(self, v):
        self._availability = v
        return self

    def set_auto_allocator(self, v):
        self._auto_allocator = v
        return self

    def set_ctv_targeting_and_attribution(self, v):
        self._ctv_targeting_and_attribution = v
        return self

    def set_pacing_mode(self, v):
        self._pacing_mode = v
        return self

    def set_partner_cpm_fee_amount(self, v):
        self._partner_cpm_fee_amount = v
        return self

    def set_partner_cpm_fee_currency(self, v):
        self._partner_cpm_fee_currency = v
        return self

    def set_partner_cpc_fee_amount(self, v):
        self._partner_cpc_fee_amount = v
        return self

    def set_partner_cpc_fee_currency(self, v):
        self._partner_cpc_fee_currency = v
        return self

    def set_max_bid_amount(self, v):
        self._max_bid_amount = v
        return self

    def set_budget_in_impressions_pre_calc(self, v):
        self._budget_in_impressions_pre_calc = v
        return self

    def set_daily_target_in_advertiser_currency(self, v):
        self._daily_target_in_advertiser_currency = v
        return self

    def set_daily_target_in_impressions(self, v):
        self._daily_target_in_impressions = v
        return self

    def set_ad_group_name(self, v):
        self._ad_group_name = v
        return self

    def set_adg_base_bid_amount(self, v):
        self._adg_base_bid_amount = v
        return self

    def set_adg_description(self, v):
        self._adg_description = v
        return self

    def set_adg_daily_budget(self, v):
        self._adg_daily_budget = v
        return self

    def set_adg_daily_budget_in_impressions(self, v):
        self._adg_daily_budget_in_impressions = v
        return self

    def set_adg_budget_in_impressions_pre_calc(self, v):
        self._adg_budget_in_impressions_pre_calc = v
        return self

    def set_adg_pacing_mode(self, v):
        self._adg_pacing_mode = v
        return self

    def set_adg_auto_allocator_priority(self, v):
        self._adg_auto_allocator_priority = v
        return self

    def set_adg_max_bid_amount(self, v):
        self._adg_max_bid_amount = v
        return self

    def set_adg_frequency_period_in_minutes(self, v):
        self._adg_frequency_period_in_minutes = v
        return self

    def set_adg_frequency_cap(self, v):
        self._adg_frequency_cap = v
        return self

    def set_adg_frequency_pricing_slope_cpm(self, v):
        self._adg_frequency_pricing_slope_cpm = v
        return self

    def set_adg_ctr_in_percent(self, v):
        self._adg_ctr_in_percent = v
        return self

    def set_device_type(self, v):
        self._device_type = v
        return self

    def set_country(self, v):
        self._country = v
        return self

    def set_category(self, v):
        self._category = v
        return self

    def set_ae_excluder(self, v):
        self._ae_excluder = v
        return self
