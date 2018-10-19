from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.tools import datetime_to_wf_format


class WFDisplayCampaignBlock(WFBlock):
    """
    @summary: Display Campaign block
    """

    template_name = 'Block - Display Campaign'

    def __init__(self):
        super(WFDisplayCampaignBlock, self).__init__(self.template_name)
        self._add_required_parameters([
            "StartDateInclusiveUTC",
            "EndDateExclusiveUTC",
            "Campaign Name",
        ])
        self._add_optional_parameters([
            "Campaign Overview",
            "PartnerCostPercentageFee",
            "Availability",
            "AutoAllocator",
            "CtvTargetingAndAttribution",
            "PacingMode",
            "PartnerCPMFeeAmount",
            "PartnerCPMFeeCurrency",
            "PartnerCPCFeeAmount",
            "PartnerCPCFeeCurrency",
            "MaxBidAmount",
            "BudgetInImpressions_preCalc",
            "DailyTargetInAdvertiserCurrency",
            "DailyTargetInImpressions",
        ])
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

        self._set_starter_task(2)

    @property
    def start_date_inclusive_utc(self):
        return self._start_date_inclusive_utc

    @start_date_inclusive_utc.setter
    def start_date_inclusive_utc(self, v):
        self._start_date_inclusive_utc = v
        self.set_parameter("Create Campaign & Flight", "StartDateInclusiveUTC", datetime_to_wf_format(v))

    @property
    def end_date_exclusive_utc(self):
        return self._end_date_exclusive_utc

    @end_date_exclusive_utc.setter
    def end_date_exclusive_utc(self, v):
        self._end_date_exclusive_utc = v
        self.set_parameter("Create Campaign & Flight", "EndDateExclusiveUTC", datetime_to_wf_format(v))

    @property
    def campaign_name(self):
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, v):
        self._campaign_name = v
        self.set_parameter("Create Campaign & Flight", "Campaign Name", v)

    @property
    def campaign_overview(self):
        return self._campaign_overview

    @campaign_overview.setter
    def campaign_overview(self, v):
        self._campaign_overview = v
        self.set_parameter("Create Campaign & Flight", "Campaign Overview", v)

    @property
    def partner_cost_percentage_fee(self):
        return self._partner_cost_percentage_fee

    @partner_cost_percentage_fee.setter
    def partner_cost_percentage_fee(self, v):
        self._partner_cost_percentage_fee = v
        self.set_parameter("Create Campaign & Flight", "PartnerCostPercentageFee", v)

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, v):
        self._availability = v
        self.set_parameter("Create Campaign & Flight", "Availability", v)

    @property
    def auto_allocator(self):
        return self._auto_allocator

    @auto_allocator.setter
    def auto_allocator(self, v):
        self._auto_allocator = v
        self.set_parameter("Create Campaign & Flight", "AutoAllocator", v)

    @property
    def ctv_targeting_and_attribution(self):
        return self._ctv_targeting_and_attribution

    @ctv_targeting_and_attribution.setter
    def ctv_targeting_and_attribution(self, v):
        self._ctv_targeting_and_attribution = v
        self.set_parameter("Create Campaign & Flight", "CtvTargetingAndAttribution", v)

    @property
    def pacing_mode(self):
        return self._pacing_mode

    @pacing_mode.setter
    def pacing_mode(self, v):
        self._pacing_mode = v
        self.set_parameter("Create Campaign & Flight", "PacingMode", v)

    @property
    def partner_cpm_fee_amount(self):
        return self._partner_cpm_fee_amount

    @partner_cpm_fee_amount.setter
    def partner_cpm_fee_amount(self, v):
        self._partner_cpm_fee_amount = v
        self.set_parameter("Create Campaign & Flight", "PartnerCPMFeeAmount", v)

    @property
    def partner_cpm_fee_currency(self):
        return self._partner_cpm_fee_currency

    @partner_cpm_fee_currency.setter
    def partner_cpm_fee_currency(self, v):
        self._partner_cpm_fee_currency = v
        self.set_parameter("Create Campaign & Flight", "PartnerCPMFeeCurrency", v)

    @property
    def partner_cpc_fee_amount(self):
        return self._partner_cpc_fee_amount

    @partner_cpc_fee_amount.setter
    def partner_cpc_fee_amount(self, v):
        self._partner_cpc_fee_amount = v
        self.set_parameter("Create Campaign & Flight", "PartnerCPCFeeAmount", v)

    @property
    def partner_cpc_fee_currency(self):
        return self._partner_cpc_fee_currency

    @partner_cpc_fee_currency.setter
    def partner_cpc_fee_currency(self, v):
        self._partner_cpc_fee_currency = v
        self.set_parameter("Create Campaign & Flight", "PartnerCPCFeeCurrency", v)

    @property
    def max_bid_amount(self):
        return self._max_bid_amount

    @max_bid_amount.setter
    def max_bid_amount(self, v):
        self._max_bid_amount = v
        self.set_parameter("Create Campaign & Flight", "MaxBidAmount", v)

    @property
    def budget_in_impressions_pre_calc(self):
        return self._budget_in_impressions_pre_calc

    @budget_in_impressions_pre_calc.setter
    def budget_in_impressions_pre_calc(self, v):
        self._budget_in_impressions_pre_calc = v
        self.set_parameter("Create Campaign & Flight", "BudgetInImpressions_preCalc", v)

    @property
    def daily_target_in_advertiser_currency(self):
        return self._daily_target_in_advertiser_currency

    @daily_target_in_advertiser_currency.setter
    def daily_target_in_advertiser_currency(self, v):
        self._daily_target_in_advertiser_currency = v
        self.set_parameter("Create Campaign & Flight", "DailyTargetInAdvertiserCurrency", v)

    @property
    def daily_target_in_impressions(self):
        return self._daily_target_in_impressions

    @daily_target_in_impressions.setter
    def daily_target_in_impressions(self, v):
        self._daily_target_in_impressions = v
        self.set_parameter("Create Campaign & Flight", "DailyTargetInImpressions", v)
