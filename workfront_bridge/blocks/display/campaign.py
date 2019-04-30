from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.tools import datetime_to_wf_format


class WFDisplayCampaignBlock(WFBlock):
    """
    @summary: Display Campaign block
    """

    template_name = 'Block - Display Campaign v2'

    block_params = {
        'Create Campaign & Flight': [
            ('Campaign Name', 'campaign_name', True),
            ('type', 'automation_type', True),
            ('StartDateTimeInclusiveUTC', 'start_date_inclusive_utc', False, datetime_to_wf_format),
            ('EndDateTimeExclusiveUTC', 'end_date_exclusive_utc', False, datetime_to_wf_format),
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
        ],
    }

    def __init__(self):
        super(WFDisplayCampaignBlock, self).__init__(self.template_name)
        self._set_starter_task(2)
        self.automation_type = 'DigitalCampaignCreate'
