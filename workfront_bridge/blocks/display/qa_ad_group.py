from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.tools import datetime_to_wf_format


class WFDisplayQAAdGroupBlock(WFBlock):
    """
    @summary: Display QA Ad Group block
    """
    template_name = 'Block - Display QA Ad Group v2'

    block_params = {
        'Ad Group QA': [
            ('StartDateTimeInclusiveUTC', 'start_date_inclusive_utc', True, datetime_to_wf_format),
            ('EndDateTimeExclusiveUTC', 'end_date_exclusive_utc', True, datetime_to_wf_format),
            ('Campaign Name', 'campaign_name', True),
            ('AdGroupName', 'ad_group_name', True),
            ('ADGBaseBidAmount', 'adg_base_bid_amount', False),
            ('Campaign Overview', 'campaign_overview', False),
            ('PartnerCostPercentageFee', 'partner_cost_percentage_fee', False),
            ('Availability', 'availability', False),
            ('AutoAllocator', 'auto_allocator', False),
            ('CtvTargetingAndAttribution', 'ctv_targeting_and_attribution', False),
            ('PacingMode', 'pacing_mode', False),
            ('PartnerCPMFeeAmount', 'partner_cpm_fee_amount', False),
            ('PartnerCPMFeeCurrency', 'partner_cpm_fee_currency', False),
            ('PartnerCPCFeeAmount', 'partner_cpc_fee_amount', False),
            ('PartnerCPCFeeCurrency', 'partner_cpc_fee_currency', False),
            ('MaxBidAmount', 'max_bid_amount', False),
            ('BudgetInImpressions_preCalc', 'budget_in_impressions_pre_calc', False),
            ('DailyTargetInAdvertiserCurrency', 'daily_target_in_advertiser_currency', False),
            ('DailyTargetInImpressions', 'daily_target_in_impressions', False),
            ('ADGDescription', 'adg_description', False),
            ('ADGDailyBudget', 'adg_daily_budget', False),
            ('ADGBudgetRate', 'adg_budget_rate', False),
            ('ADGDailyBudgetInImpressions', 'adg_daily_budget_in_impressions', False),
            ('ADGBudgetInImpressions_preCalc', 'adg_budget_in_impressions_pre_calc', False),
            ('ADGPacingMode', 'adg_pacing_mode', False),
            ('ADGAutoAllocatorPriority', 'adg_auto_allocator_priority', False),
            ('ADGMaxBidAmount', 'adg_max_bid_amount', False),
            ('ADGFrequencyPeriodInMinutes', 'adg_frequency_period_in_minutes', False),
            ('ADGFrequencyCap', 'adg_frequency_cap', False),
            ('ADGFrequencyPricingSlopeCPM', 'adg_frequency_pricing_slope_cpm', False),
            ('ADGKPIGoal', 'adg_kpi_goal', False),
            ('ADGCTRInPercent', 'adg_ctr_in_percent', False),
            ('ADGCPAInAmount', 'adg_cpa_in_amount', False),
            ('Device Type', 'device_type', False, lambda l: l),
            ('Country', 'country', False, lambda l: l),
            ('Category', 'category', False),
            ('AEExcluder', 'ae_excluder', False),
        ],
    }
