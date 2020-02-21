from workfront_bridge.blocks.base import WFBlock


class WFDisplayCreateAdGroupBlock(WFBlock):
    """
    @summary: Display Create Ad Group block
    """

    template_name = 'Block - Display Create Ad Group'

    block_params = {
        'Create Ad Group': [
            ('AdGroupName', 'ad_group_name', True),
            ('type', 'automation_type', True),
            ('ADGDescription', 'adg_description', False),
            ('ADGDailyBudget', 'adg_daily_budget', False),
            ('ADGDailyBudgetInImpressions', 'adg_daily_budget_in_impressions', False),
            ('ADGBudgetInImpressions_preCalc', 'adg_budget_in_impressions_pre_calc', False),
            ('ADGPacingMode', 'adg_pacing_mode', False),
            ('ADGAutoAllocatorPriority', 'adg_auto_allocator_priority', False),
            ('ADGMaxBidAmount', 'adg_max_bid_amount', False),
            ('ADGBudgetRate', 'adg_budget_rate', False),
            ('ADGFrequencyPeriodInMinutes', 'adg_frequency_period_in_minutes', False),
            ('ADGFrequencyCap', 'adg_frequency_cap', False),
            ('ADGFrequencyPricingSlopeCPM', 'adg_frequency_pricing_slope_cpm', False),
            ('ADGCTRInPercent', 'adg_ctr_in_percent', False),
            ('ADGBaseBidAmount', 'adg_base_bid_amount', False),
            ('Device Type', 'device_type', False, lambda l: l),
            ('Country', 'country', False, lambda l: l),
            ('Category', 'category', False),
            ('AEExcluder', 'ae_excluder', False),
        ],
    }

    def __init__(self):
        super(WFDisplayCreateAdGroupBlock, self).__init__(self.template_name)
        self.automation_type = 'DigitalDisplayAdGroupCreate'
