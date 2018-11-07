from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.tools import datetime_to_wf_format


class WFSocialAdGroupCreateBlock(WFBlock):
    """
    @summary: Social Ad Group Create block. Spending and schedule information.
    """

    template_name = 'Block - Social Ad Group Create'
    create_ad_group_task_name = 'Ad Group Create'

    def __init__(self):
        super(WFSocialAdGroupCreateBlock, self).__init__(self.template_name)
        self._add_required_parameters([
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
            'FB/Instagram Facebook Platforms',
            'FB/Instagram Instagram Platforms',
            'FB/Instagram Audience Network Platforms',
            'FB/Instagram Messenger Platforms'
        ])
        self._bid_amount = None
        self._impressions_or_clicks = None
        self._number_of_impressions = None
        self._budget_daily_or_lifetime = None
        self._datetime_start = None
        self._datetime_end = None
        self._device_type = None
        self._mobile_os = None
        self._exclude_categories = None
        self._fb_facebook_placement = None
        self._fb_instagram_placement = None
        self._fb_audience_placement = None
        self._fb_messenger_placement = None

    @property
    def bid_amount(self):
        return self._bid_amount

    @bid_amount.setter
    def bid_amount(self, v):
        self._bid_amount = v
        self.set_parameter(self.create_ad_group_task_name, 'Social Bid Amount', v)

    @property
    def impressions_or_clicks(self):
        return self._impressions_or_clicks

    @impressions_or_clicks.setter
    def impressions_or_clicks(self, v):
        self._impressions_or_clicks = v
        self.set_parameter(self.create_ad_group_task_name, 'Social Impressions/Clicks', v)

    @property
    def number_of_impressions(self):
        return self._number_of_impressions

    @number_of_impressions.setter
    def number_of_impressions(self, v):
        self._number_of_impressions = v
        self.set_parameter(self.create_ad_group_task_name, 'Social Number of impressions', v)

    @property
    def budget_daily_or_lifetime(self):
        return self._budget_daily_or_lifetime

    @budget_daily_or_lifetime.setter
    def budget_daily_or_lifetime(self, v):
        self._budget_daily_or_lifetime = v
        self.set_parameter(self.create_ad_group_task_name, 'Social Daily/Lifetime Budget', v)

    @property
    def datetime_start(self):
        return self._datetime_start

    @datetime_start.setter
    def datetime_start(self, v):
        self._datetime_start = v
        self.set_parameter(self.create_ad_group_task_name, 'Social Start Date & Time', datetime_to_wf_format(v))

    @property
    def datetime_end(self):
        return self._datetime_end

    @datetime_end.setter
    def datetime_end(self, v):
        self._datetime_end = v
        self.set_parameter(self.create_ad_group_task_name, 'Social End Date & Time', datetime_to_wf_format(v))

    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, v):
        self._device_type = v
        self.set_parameter(self.create_ad_group_task_name, 'Social Device Type', v)

    @property
    def mobile_os(self):
        return self._mobile_os

    @mobile_os.setter
    def mobile_os(self, v):
        self._mobile_os = v
        self.set_parameter(self.create_ad_group_task_name, 'Social Mobile Operating System', v)

    @property
    def exclude_categories(self):
        return self._exclude_categories

    @exclude_categories.setter
    def exclude_categories(self, v):
        self._exclude_categories = v
        if v:
            self.set_parameter(self.create_ad_group_task_name, 'Social Exclude Categories', v)

    @property
    def fb_facebook_placement(self):
        return self._fb_facebook_placement

    @fb_facebook_placement.setter
    def fb_facebook_placement(self, v):
        self._fb_facebook_placement = v
        if v:
            self.set_parameter(self.create_ad_group_task_name, 'FB/Instagram Facebook Platforms', v)

    @property
    def fb_instagram_placement(self):
        return self._fb_instagram_placement

    @fb_instagram_placement.setter
    def fb_instagram_placement(self, v):
        self._fb_instagram_placement = v
        if v:
            self.set_parameter(self.create_ad_group_task_name, 'FB/Instagram Facebook Platforms', v)

    @property
    def fb_audience_placement(self):
        return self._fb_audience_placement

    @fb_audience_placement.setter
    def fb_audience_placement(self, v):
        self._fb_audience_placement = v
        if v:
            self.set_parameter(self.create_ad_group_task_name, 'FB/Instagram Facebook Platforms', v)

    @property
    def fb_messenger_placement(self):
        return self._fb_messenger_placement

    @fb_messenger_placement.setter
    def fb_messenger_placement(self, v):
        self._fb_messenger_placement = v
        if v:
            self.set_parameter(self.create_ad_group_task_name, 'FB/Instagram Facebook Platforms', v)
