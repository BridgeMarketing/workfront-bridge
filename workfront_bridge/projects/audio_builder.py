from workfront_bridge.blocks.audio.campaign import WFAudioCampaignBlock
from workfront_bridge.blocks.audio.ad_group_create import WFAudioCreateAdGroupBlock
from workfront_bridge.blocks.audio.ad_group_creative_upload import WFAudioCreativeUploadBlock
from workfront_bridge.blocks.display.data import WFDisplayDataBlock
from workfront_bridge.blocks.display.launch import WFDisplayLaunchBlock
from workfront_bridge.blocks.display.ad_group_setup import WFDisplayAdGroupSetupBlock
from workfront_bridge.projects.audio import WFProjectAudioContainer
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.blocks.base import WFBlockParser


class AudioProjectBuilder(object):
    """
    @summary: Audio project builder
    """

    ad_group_params = [
        "ad_group_name",
        "adg_base_bid_amount",
        "adg_description",
        "adg_budget_rate",
        "adg_daily_budget",
        "adg_daily_budget_in_impressions",
        "adg_budget_in_impressions_pre_calc",
        "adg_pacing_mode",
        "adg_auto_allocator_priority",
        "adg_max_bid_amount",
        "adg_frequency_period_in_minutes",
        "adg_frequency_cap",
        "adg_frequency_pricing_slope_cpm",
        "adg_ctr_in_percent",
        "device_type",
        "country",
        "category",
        "ae_excluder",
        "creatives",  # Nested
    ]
    creative_upload_params = [
        "creative_name",
        "media_s3_url",
        "third_party_impression_tracking_url",
        "clickthrough_url",
        "landing_page_url",
        "duration",
    ]
    creative_qa_params = [
        "creative_name",
        "media_s3_url",
        "third_party_impression_tracking_url",
        "clickthrough_url",
        "landing_page_url",
        "duration",
    ]

    def __init__(self, wf, project_name):
        """
        @param wf: Workfront service object
        @param project_name: project name in Workfront
        """
        self.project_name = project_name
        self.wf = wf
        self.ad_groups = []

        # project level
        self._ttd_audience_id = None
        self._ttd_campaign_id = None
        self._ttd_flight_id = None
        self._ttd_creative_id = None
        self._ttd_advertiser_id = None
        self._ttd_bonus_media_advertiser_id = None
        self._lr_account_id = None
        self._lr_bonus_media_account_id = None
        self._is_targeted_bonus_media = None
        self._ttd_tracking_tags = None
        self._multiple_ad_groups = None
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

    def add_ad_group(self, **kwargs):
        allowed_kwargs = self.ad_group_params
        creative_kwargs = set(self.creative_upload_params + self.creative_qa_params)

        ad_group = {}
        for k, v in kwargs.items():
            if k not in allowed_kwargs:
                raise WFBrigeException('Invalid Key {}'.format(k))
            elif k == 'creatives':
                ad_group['creatives'] = []
                for creative in v:
                    ad_group_creative = {}
                    for creative_key, creative_value in creative.items():
                        if creative_key not in creative_kwargs:
                            raise WFBrigeException('Invalid Key {}'.format(creative_key))
                        ad_group_creative[creative_key] = creative_value
                    ad_group['creatives'].append(ad_group_creative)
            else:
                ad_group[k] = v
        self.ad_groups.append(ad_group)

    def build_project(self, container_class=WFProjectAudioContainer):
        project = container_class(self.project_name)
        project.ttd_audience_id = self._ttd_audience_id
        project.ttd_campaign_id = self._ttd_campaign_id
        project.ttd_flight_id = self._ttd_flight_id
        project.ttd_creative_id = self._ttd_creative_id
        project.ttd_advertiser_id = self._ttd_advertiser_id
        project.ttd_bonus_media_advertiser_id = self._ttd_bonus_media_advertiser_id
        project.lr_account_id = self._lr_account_id
        project.lr_bonus_media_account_id = self._lr_bonus_media_account_id 
        project.is_targeted_bonus_media = self._is_targeted_bonus_media
        project.ttd_tracking_tags = self._ttd_tracking_tags
        project.multiple_ad_groups = self._multiple_ad_groups
        project.project_type = self._project_type
        return project

    def build_data_block(self):
        data_block = WFDisplayDataBlock()
        data_block.audience_name = self._audience_name
        return data_block

    def build_campaign_block(self, campaign_block_class=WFAudioCampaignBlock):
        campaign_block = campaign_block_class()
        campaign_block.start_date_inclusive_utc = self._start_date_inclusive_utc
        campaign_block.end_date_exclusive_utc = self._end_date_exclusive_utc
        campaign_block.campaign_name = self._campaign_name
        campaign_block.campaign_overview = self._campaign_overview
        campaign_block.partner_cost_percentage_fee = self._partner_cost_percentage_fee
        campaign_block.availability = self._availability
        campaign_block.auto_allocator = self._auto_allocator
        campaign_block.ctv_targeting_and_attribution = self._ctv_targeting_and_attribution
        campaign_block.pacing_mode = self._pacing_mode
        campaign_block.partner_cpm_fee_amount = self._partner_cpm_fee_amount
        campaign_block.partner_cpm_fee_currency = self._partner_cpm_fee_currency
        campaign_block.partner_cpc_fee_amount = self._partner_cpc_fee_amount
        campaign_block.partner_cpc_fee_currency = self._partner_cpc_fee_currency
        campaign_block.max_bid_amount = self._max_bid_amount
        campaign_block.budget_in_impressions_pre_calc = self._budget_in_impressions_pre_calc
        campaign_block.daily_target_in_advertiser_currency = self._daily_target_in_advertiser_currency
        campaign_block.daily_target_in_impressions = self._daily_target_in_impressions
        return campaign_block

    def build_ad_groups(self,
                        create_ad_group_class=WFAudioCreateAdGroupBlock,
                        creative_upload_class=WFAudioCreativeUploadBlock):
        ad_group_setup_blocks = []

        for ad_group in self.ad_groups:
            ad_group_setup_block = WFDisplayAdGroupSetupBlock()

            for creative in ad_group['creatives']:
                creative_upload_dict = {k: creative[k]
                                        for k in self.creative_upload_params
                                        if k in creative}
                ad_group_setup_block.add_creative(block_class=creative_upload_class, **creative_upload_dict)

            ad_group_setup_block.add_ad_group(block_class=create_ad_group_class, **ad_group)
            ad_group_setup_blocks.append(ad_group_setup_block)
            ad_group.update({
                'start_date_inclusive_utc': self._start_date_inclusive_utc,
                'end_date_exclusive_utc': self._end_date_exclusive_utc,
                'campaign_name': self._campaign_name,
                'campaign_overview': self._campaign_overview,
                'partner_cost_percentage_fee': self._partner_cost_percentage_fee,
                'availability': self._availability,
                'auto_allocator': self._auto_allocator,
                'ctv_targeting_and_attribution': self._ctv_targeting_and_attribution,
                'pacing_mode': self._pacing_mode,
                'partner_cpm_fee_amount': self._partner_cpm_fee_amount,
                'partner_cpm_fee_currency': self._partner_cpm_fee_currency,
                'partner_cpc_fee_amount': self._partner_cpc_fee_amount,
                'partner_cpc_fee_currency': self._partner_cpc_fee_currency,
                'max_bid_amount': self._max_bid_amount,
                'budget_in_impressions_pre_calc': self._budget_in_impressions_pre_calc,
                'daily_target_in_advertiser_currency': self._daily_target_in_advertiser_currency,
                'daily_target_in_impressions': self._daily_target_in_impressions,
            })

        return ad_group_setup_blocks

    def build(self):
        """
        @summary: build the Workfront project.
        @raise WFBrigeException
        @return: WFProject object
        """

        project = self.build_project()
        data_block = self.build_data_block()
        campaign_block = self.build_campaign_block()
        ad_group_setup_blocks = self.build_ad_groups()

        project_blocks = [
            data_block,
            campaign_block,
        ]
        project_blocks.extend(ad_group_setup_blocks)
        [project.append(block) for block in project_blocks]

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)
        return wf_project

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
    
    def set_ttd_bonus_media_advertiser_id(self, v):
        self._ttd_bonus_media_advertiser_id = v
        return self

    def set_lr_account_id(self, v):
        self._lr_account_id = v
        return self

    def set_lr_bonus_media_account_id(self, v):
        self._lr_bonus_media_account_id = v
        return self

    def set_is_targeted_bonus_media(self, v):
        self._is_targeted_bonus_media = v
        return self

    def set_ttd_tracking_tags(self, v):
        self._ttd_tracking_tags = v
        return self

    def set_multiple_ad_groups(self, v):
        self._multiple_ad_groups = v
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
