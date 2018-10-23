from workfront_bridge.blocks.base import WFBlock


class WFDisplayAdGroupBlock(WFBlock):
    """
    @summary: Display Ad Group block
    """

    template_name = 'Block - Display Ad Group'

    def __init__(self):
        super(WFDisplayAdGroupBlock, self).__init__(self.template_name)
        self._add_required_parameters([
            "AdGroupName",
        ])
        self._add_optional_parameters([
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
            "ADGBaseBidAmount",
            "Device Type",
            "Country",
            "Category",
            "AEExcluder",
        ])
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

        self._set_starter_task(2)

    @property
    def ad_group_name(self):
        return self._ad_group_name

    @ad_group_name.setter
    def ad_group_name(self, v):
        self._ad_group_name = v
        self.set_parameter("Create Ad Group", "AdGroupName", v)

    @property
    def adg_base_bid_amount(self):
        return self._adg_base_bid_amount

    @adg_base_bid_amount.setter
    def adg_base_bid_amount(self, v):
        self._adg_base_bid_amount = v
        self.set_parameter("Create Ad Group", "ADGBaseBidAmount", v)

    @property
    def adg_description(self):
        return self._adg_description

    @adg_description.setter
    def adg_description(self, v):
        self._adg_description = v
        self.set_parameter("Create Ad Group", "ADGDescription", v)

    @property
    def adg_daily_budget(self):
        return self._adg_daily_budget

    @adg_daily_budget.setter
    def adg_daily_budget(self, v):
        self._adg_daily_budget = v
        self.set_parameter("Create Ad Group", "ADGDailyBudget", v)

    @property
    def adg_daily_budget_in_impressions(self):
        return self._adg_daily_budget_in_impressions

    @adg_daily_budget_in_impressions.setter
    def adg_daily_budget_in_impressions(self, v):
        self._adg_daily_budget_in_impressions = v
        self.set_parameter("Create Ad Group", "ADGDailyBudgetInImpressions", v)

    @property
    def adg_budget_in_impressions_pre_calc(self):
        return self._adg_budget_in_impressions_pre_calc

    @adg_budget_in_impressions_pre_calc.setter
    def adg_budget_in_impressions_pre_calc(self, v):
        self._adg_budget_in_impressions_pre_calc = v
        self.set_parameter("Create Ad Group", "ADGBudgetInImpressions_preCalc", v)

    @property
    def adg_pacing_mode(self):
        return self._adg_pacing_mode

    @adg_pacing_mode.setter
    def adg_pacing_mode(self, v):
        self._adg_pacing_mode = v
        self.set_parameter("Create Ad Group", "ADGPacingMode", v)

    @property
    def adg_auto_allocator_priority(self):
        return self._adg_auto_allocator_priority

    @adg_auto_allocator_priority.setter
    def adg_auto_allocator_priority(self, v):
        self._adg_auto_allocator_priority = v
        self.set_parameter("Create Ad Group", "ADGAutoAllocatorPriority", v)

    @property
    def adg_max_bid_amount(self):
        return self._adg_max_bid_amount

    @adg_max_bid_amount.setter
    def adg_max_bid_amount(self, v):
        self._adg_max_bid_amount = v
        self.set_parameter("Create Ad Group", "ADGMaxBidAmount", v)

    @property
    def adg_frequency_period_in_minutes(self):
        return self._adg_frequency_period_in_minutes

    @adg_frequency_period_in_minutes.setter
    def adg_frequency_period_in_minutes(self, v):
        self._adg_frequency_period_in_minutes = v
        self.set_parameter("Create Ad Group", "ADGFrequencyPeriodInMinutes", v)

    @property
    def adg_frequency_cap(self):
        return self._adg_frequency_cap

    @adg_frequency_cap.setter
    def adg_frequency_cap(self, v):
        self._adg_frequency_cap = v
        self.set_parameter("Create Ad Group", "ADGFrequencyCap", v)

    @property
    def adg_frequency_pricing_slope_cpm(self):
        return self._adg_frequency_pricing_slope_cpm

    @adg_frequency_pricing_slope_cpm.setter
    def adg_frequency_pricing_slope_cpm(self, v):
        self._adg_frequency_pricing_slope_cpm = v
        self.set_parameter("Create Ad Group", "ADGFrequencyPricingSlopeCPM", v)

    @property
    def adg_ctr_in_percent(self):
        return self._adg_ctr_in_percent

    @adg_ctr_in_percent.setter
    def adg_ctr_in_percent(self, v):
        self._adg_ctr_in_percent = v
        self.set_parameter("Create Ad Group", "ADGCTRInPercent", v)

    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, v):
        self._device_type = v
        self.set_parameter("Create Ad Group", "Device Type", v)

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, v):
        self._country = v
        self.set_parameter("Create Ad Group", "Country", v)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, v):
        self._category = v
        self.set_parameter("Create Ad Group", "Category", v)

    @property
    def ae_excluder(self):
        return self._ae_excluder

    @ae_excluder.setter
    def ae_excluder(self, v):
        self._ae_excluder = v
        self.set_parameter("Create Ad Group", "AEExcluder", v)
