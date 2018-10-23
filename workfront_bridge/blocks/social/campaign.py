from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.tools import datetime_to_wf_format


class WFSocialSetupBlock(WFBlock):
    """
    @summary: Social Setup block. Campaign information.
    """

    template_name = 'Block - Social Setup'
    create_campaign_task_name = 'Create Campaign'

    def __init__(self):
        super(WFSocialSetupBlock, self).__init__(self.template_name)
        self._set_starter_task(2)

        self._add_required_parameters([
            'Social Campaign Title',
            'Social Bid Amount',
            'Social Impressions/Clicks',
            'Social Number of impressions',
            'Social Daily/Lifetime Budget',
            'Social Start Date & Time',
            'Social End Date & Time',
            'Social Device Type',
            'Social Mobile Operating System',
        ])
        self._add_optional_parameters([
            'Social Exclude Categories',
            'FB/Instagram Advertising Objective',
            'FB/Instagram Offer',
            'FB/Instagram Apply Block List',
        ])

        self._campaign_title = None
        self._bid_amount = None
        self._impressions_or_clicks = None
        self._number_of_impressions = None
        self._budget_daily_or_lifetime = None
        self._datetime_start = None
        self._datetime_end = None
        self._device_type = None
        self._mobile_os = None
        self._exclude_categories = None
        self._fb_advertising_objective = None
        self._fb_offer = None
        self._fb_apply_block_list = None

    @property
    def campaign_title(self):
        return self._campaign_title

    @campaign_title.setter
    def campaign_title(self, v):
        self._campaign_title = v
        self.set_parameter(self.create_campaign_task_name, 'Social Campaign Title', v)

    @property
    def bid_amount(self):
        return self._bid_amount

    @bid_amount.setter
    def bid_amount(self, v):
        self._bid_amount = v
        self.set_parameter(self.create_campaign_task_name, 'Social Bid Amount', v)

    @property
    def impressions_or_clicks(self):
        return self._impressions_or_clicks

    @impressions_or_clicks.setter
    def impressions_or_clicks(self, v):
        self._impressions_or_clicks = v
        self.set_parameter(self.create_campaign_task_name, 'Social Impressions/Clicks', v)

    @property
    def number_of_impressions(self):
        return self._number_of_impressions

    @number_of_impressions.setter
    def number_of_impressions(self, v):
        self._number_of_impressions = v
        self.set_parameter(self.create_campaign_task_name, 'Social Number of impressions', v)

    @property
    def budget_daily_or_lifetime(self):
        return self._budget_daily_or_lifetime

    @budget_daily_or_lifetime.setter
    def budget_daily_or_lifetime(self, v):
        self._budget_daily_or_lifetime = v
        self.set_parameter(self.create_campaign_task_name, 'Social Daily/Lifetime Budget', v)

    @property
    def datetime_start(self):
        return self._datetime_start

    @datetime_start.setter
    def datetime_start(self, v):
        self._datetime_start = v
        self.set_parameter(self.create_campaign_task_name, 'Social Start Date & Time', datetime_to_wf_format(v))

    @property
    def datetime_end(self):
        return self._datetime_end

    @datetime_end.setter
    def datetime_end(self, v):
        self._datetime_end = v
        self.set_parameter(self.create_campaign_task_name, 'Social End Date & Time', datetime_to_wf_format(v))

    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, v):
        self._device_type = v
        self.set_parameter(self.create_campaign_task_name, 'Social Device Type', v)

    @property
    def mobile_os(self):
        return self._mobile_os

    @mobile_os.setter
    def mobile_os(self, v):
        self._mobile_os = v
        self.set_parameter(self.create_campaign_task_name, 'Social Mobile Operating System', v)

    @property
    def exclude_categories(self):
        return self._exclude_categories

    @exclude_categories.setter
    def exclude_categories(self, v):
        self._exclude_categories = v
        if v:
            self.set_parameter(self.create_campaign_task_name, 'Social Exclude Categories', v)

    @property
    def fb_advertising_objective(self):
        return self._fb_advertising_objective

    @fb_advertising_objective.setter
    def fb_advertising_objective(self, v):
        self._fb_advertising_objective = v
        self.set_parameter(self.create_campaign_task_name, 'FB/Instagram Advertising Objective', v)

    @property
    def fb_offer(self):
        return self._fb_offer

    @fb_offer.setter
    def fb_offer(self, v):
        self._fb_offer = v
        self.set_parameter(self.create_campaign_task_name, 'FB/Instagram Offer', v)

    @property
    def fb_apply_block_list(self):
        return self._fb_apply_block_list

    @fb_apply_block_list.setter
    def fb_apply_block_list(self, v):
        self._fb_apply_block_list = v
        self.set_parameter(self.create_campaign_task_name, 'FB/Instagram Apply Block List', v)
