from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.tools import datetime_to_wf_format


class WFDisplayQAFinalReviewBlock(WFBlock):
    """
    @summary: Display QA Final Review block
    """
    template_name = 'Block - Display QA Final Review'

    def __init__(self):
        super(WFDisplayQAFinalReviewBlock, self).__init__(self.template_name)
        self._add_required_parameters([
            "StartDateInclusiveUTC",
            "EndDateExclusiveUTC",
            "Campaign Name",
            "AdGroupName",
            "ADGBaseBidAmount",
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
            "ADGDescription",
            "ADGDailyBudget",
            "ADGDailyBudgetInImpressions",
            "ADGBudgetInImpressions_preCalc",
            "ADGPacingMode",
            "ADGAutoAllocatorPriority",
            "ADGMaxBidAmount",
            "ADGFrequencyPeriodInMinutes",
            "ADGFrequencyCap",
            "ADGFrequencyPricingSlopeCPM",
            "ADGCTRInPercent",
            "Device Type",
            "Country",
            "Category",
            "AEExcluder",
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

    @property
    def start_date_inclusive_utc(self):
        return self._start_date_inclusive_utc

    @start_date_inclusive_utc.setter
    def start_date_inclusive_utc(self, v):
        self._start_date_inclusive_utc = v
        self.set_parameter("Final review of Campaign in TTD", "StartDateInclusiveUTC", datetime_to_wf_format(v))

    @property
    def end_date_exclusive_utc(self):
        return self._end_date_exclusive_utc

    @end_date_exclusive_utc.setter
    def end_date_exclusive_utc(self, v):
        self._end_date_exclusive_utc = v
        self.set_parameter("Final review of Campaign in TTD", "EndDateExclusiveUTC", datetime_to_wf_format(v))

    @property
    def campaign_name(self):
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, v):
        self._campaign_name = v
        self.set_parameter("Final review of Campaign in TTD", "Campaign Name", v)

    @property
    def campaign_overview(self):
        return self._campaign_overview

    @campaign_overview.setter
    def campaign_overview(self, v):
        self._campaign_overview = v
        self.set_parameter("Final review of Campaign in TTD", "Campaign Overview", v)

    @property
    def partner_cost_percentage_fee(self):
        return self._partner_cost_percentage_fee

    @partner_cost_percentage_fee.setter
    def partner_cost_percentage_fee(self, v):
        self._partner_cost_percentage_fee = v
        self.set_parameter("Final review of Campaign in TTD", "PartnerCostPercentageFee", v)

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, v):
        self._availability = v
        self.set_parameter("Final review of Campaign in TTD", "Availability", v)

    @property
    def auto_allocator(self):
        return self._auto_allocator

    @auto_allocator.setter
    def auto_allocator(self, v):
        self._auto_allocator = v
        self.set_parameter("Final review of Campaign in TTD", "AutoAllocator", v)

    @property
    def ctv_targeting_and_attribution(self):
        return self._ctv_targeting_and_attribution

    @ctv_targeting_and_attribution.setter
    def ctv_targeting_and_attribution(self, v):
        self._ctv_targeting_and_attribution = v
        self.set_parameter("Final review of Campaign in TTD", "CtvTargetingAndAttribution", v)

    @property
    def pacing_mode(self):
        return self._pacing_mode

    @pacing_mode.setter
    def pacing_mode(self, v):
        self._pacing_mode = v
        self.set_parameter("Final review of Campaign in TTD", "PacingMode", v)

    @property
    def partner_cpm_fee_amount(self):
        return self._partner_cpm_fee_amount

    @partner_cpm_fee_amount.setter
    def partner_cpm_fee_amount(self, v):
        self._partner_cpm_fee_amount = v
        self.set_parameter("Final review of Campaign in TTD", "PartnerCPMFeeAmount", v)

    @property
    def partner_cpm_fee_currency(self):
        return self._partner_cpm_fee_currency

    @partner_cpm_fee_currency.setter
    def partner_cpm_fee_currency(self, v):
        self._partner_cpm_fee_currency = v
        self.set_parameter("Final review of Campaign in TTD", "PartnerCPMFeeCurrency", v)

    @property
    def partner_cpc_fee_amount(self):
        return self._partner_cpc_fee_amount

    @partner_cpc_fee_amount.setter
    def partner_cpc_fee_amount(self, v):
        self._partner_cpc_fee_amount = v
        self.set_parameter("Final review of Campaign in TTD", "PartnerCPCFeeAmount", v)

    @property
    def partner_cpc_fee_currency(self):
        return self._partner_cpc_fee_currency

    @partner_cpc_fee_currency.setter
    def partner_cpc_fee_currency(self, v):
        self._partner_cpc_fee_currency = v
        self.set_parameter("Final review of Campaign in TTD", "PartnerCPCFeeCurrency", v)

    @property
    def max_bid_amount(self):
        return self._max_bid_amount

    @max_bid_amount.setter
    def max_bid_amount(self, v):
        self._max_bid_amount = v
        self.set_parameter("Final review of Campaign in TTD", "MaxBidAmount", v)

    @property
    def budget_in_impressions_pre_calc(self):
        return self._budget_in_impressions_pre_calc

    @budget_in_impressions_pre_calc.setter
    def budget_in_impressions_pre_calc(self, v):
        self._budget_in_impressions_pre_calc = v
        self.set_parameter("Final review of Campaign in TTD", "BudgetInImpressions_preCalc", v)

    @property
    def daily_target_in_advertiser_currency(self):
        return self._daily_target_in_advertiser_currency

    @daily_target_in_advertiser_currency.setter
    def daily_target_in_advertiser_currency(self, v):
        self._daily_target_in_advertiser_currency = v
        self.set_parameter("Final review of Campaign in TTD", "DailyTargetInAdvertiserCurrency", v)

    @property
    def daily_target_in_impressions(self):
        return self._daily_target_in_impressions

    @daily_target_in_impressions.setter
    def daily_target_in_impressions(self, v):
        self._daily_target_in_impressions = v
        self.set_parameter("Final review of Campaign in TTD", "DailyTargetInImpressions", v)

    @property
    def ad_group_name(self):
        return self._ad_group_name

    @ad_group_name.setter
    def ad_group_name(self, v):
        self._ad_group_name = v
        self.set_parameter("Final review of Campaign in TTD", "AdGroupName", v)

    @property
    def adg_base_bid_amount(self):
        return self._adg_base_bid_amount

    @adg_base_bid_amount.setter
    def adg_base_bid_amount(self, v):
        self._adg_base_bid_amount = v
        self.set_parameter("Final review of Campaign in TTD", "ADGBaseBidAmount", v)

    @property
    def adg_description(self):
        return self._adg_description

    @adg_description.setter
    def adg_description(self, v):
        self._adg_description = v
        self.set_parameter("Final review of Campaign in TTD", "ADGDescription", v)

    @property
    def adg_daily_budget(self):
        return self._adg_daily_budget

    @adg_daily_budget.setter
    def adg_daily_budget(self, v):
        self._adg_daily_budget = v
        self.set_parameter("Final review of Campaign in TTD", "ADGDailyBudget", v)

    @property
    def adg_daily_budget_in_impressions(self):
        return self._adg_daily_budget_in_impressions

    @adg_daily_budget_in_impressions.setter
    def adg_daily_budget_in_impressions(self, v):
        self._adg_daily_budget_in_impressions = v
        self.set_parameter("Final review of Campaign in TTD", "ADGDailyBudgetInImpressions", v)

    @property
    def adg_budget_in_impressions_pre_calc(self):
        return self._adg_budget_in_impressions_pre_calc

    @adg_budget_in_impressions_pre_calc.setter
    def adg_budget_in_impressions_pre_calc(self, v):
        self._adg_budget_in_impressions_pre_calc = v
        self.set_parameter("Final review of Campaign in TTD", "ADGBudgetInImpressions_preCalc", v)

    @property
    def adg_pacing_mode(self):
        return self._adg_pacing_mode

    @adg_pacing_mode.setter
    def adg_pacing_mode(self, v):
        self._adg_pacing_mode = v
        self.set_parameter("Final review of Campaign in TTD", "ADGPacingMode", v)

    @property
    def adg_auto_allocator_priority(self):
        return self._adg_auto_allocator_priority

    @adg_auto_allocator_priority.setter
    def adg_auto_allocator_priority(self, v):
        self._adg_auto_allocator_priority = v
        self.set_parameter("Final review of Campaign in TTD", "ADGAutoAllocatorPriority", v)

    @property
    def adg_max_bid_amount(self):
        return self._adg_max_bid_amount

    @adg_max_bid_amount.setter
    def adg_max_bid_amount(self, v):
        self._adg_max_bid_amount = v
        self.set_parameter("Final review of Campaign in TTD", "ADGMaxBidAmount", v)

    @property
    def adg_frequency_period_in_minutes(self):
        return self._adg_frequency_period_in_minutes

    @adg_frequency_period_in_minutes.setter
    def adg_frequency_period_in_minutes(self, v):
        self._adg_frequency_period_in_minutes = v
        self.set_parameter("Final review of Campaign in TTD", "ADGFrequencyPeriodInMinutes", v)

    @property
    def adg_frequency_cap(self):
        return self._adg_frequency_cap

    @adg_frequency_cap.setter
    def adg_frequency_cap(self, v):
        self._adg_frequency_cap = v
        self.set_parameter("Final review of Campaign in TTD", "ADGFrequencyCap", v)

    @property
    def adg_frequency_pricing_slope_cpm(self):
        return self._adg_frequency_pricing_slope_cpm

    @adg_frequency_pricing_slope_cpm.setter
    def adg_frequency_pricing_slope_cpm(self, v):
        self._adg_frequency_pricing_slope_cpm = v
        self.set_parameter("Final review of Campaign in TTD", "ADGFrequencyPricingSlopeCPM", v)

    @property
    def adg_ctr_in_percent(self):
        return self._adg_ctr_in_percent

    @adg_ctr_in_percent.setter
    def adg_ctr_in_percent(self, v):
        self._adg_ctr_in_percent = v
        self.set_parameter("Final review of Campaign in TTD", "ADGCTRInPercent", v)

    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, v):
        self._device_type = v
        self.set_parameter("Final review of Campaign in TTD", "Device Type", v)

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, v):
        self._country = v
        self.set_parameter("Final review of Campaign in TTD", "Country", v)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, v):
        self._category = v
        self.set_parameter("Final review of Campaign in TTD", "Category", v)

    @property
    def ae_excluder(self):
        return self._ae_excluder

    @ae_excluder.setter
    def ae_excluder(self, v):
        self._ae_excluder = v
        self.set_parameter("Final review of Campaign in TTD", "AEExcluder", v)
