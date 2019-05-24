from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.tools import datetime_to_wf_format


class WFSocialAdGroupCreateBlock(WFBlock):
    """
    @summary: Social Ad Group Create block. Spending and schedule information.
    """

    template_name = 'Block - Social Ad Group Create'

    block_params = {
        'Ad Group Create': [
            ('Social Bid Amount', 'bid_amount', True),
            ('Social Impressions/Clicks', 'impressions_or_clicks', True),
            ('Social Number of impressions', 'number_of_impressions', True),
            ('Social Daily/Lifetime Budget', 'budget_daily_or_lifetime', True),
            ('Social Start Date & Time', 'datetime_start', True, datetime_to_wf_format),
            ('Social End Date & Time', 'datetime_end', True, datetime_to_wf_format),
            ('Social Device Type', 'device_type', True, lambda l: l),
            ('Social Mobile Operating System', 'mobile_os', True, lambda l: l),
            ('FB/Instagram Placement', 'fb_placement', True),
            ('Social Exclude Categories', 'exclude_categories', False),
        ],
    }
