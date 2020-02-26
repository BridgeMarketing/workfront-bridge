from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.tools import datetime_to_wf_format


class WFProjectDisplayContainer(WFBlock):
    """
    @summary: Workfront Display Project Container.
    Use this project container to create Workfront display projects.
    The container has no preset tasks, but it has the project level fields.
    """

    template_name = "Base Project Container - Display Channel v2"

    block_params = {
        '': [
            ('TTDAdvertiserID', 'ttd_advertiser_id', True),
            ('TTDAdvertiserBonusMediaID', 'ttd_bonus_media_advertiser_id', True), 
            ('LiveRampAccountID', 'lr_account_id', True),
            ('LiveRampAccountBonusMediaID', 'lr_bonus_media_account_id', True),
            ('TTDAudienceID', 'ttd_audience_id', False),
            ('TTDCampaignID', 'ttd_campaign_id', False),
            ('TTDFlightID', 'ttd_flight_id', False),
            ('TTDCreativeID', 'ttd_creative_id', False),
            ('IsTargetedBonusMedia', 'is_targeted_bonus_media', False),
            ('TTDTrackingTags', 'ttd_tracking_tags', False),
            ('MultipleAdGroups', 'multiple_ad_groups', False),
            ('Project Type', 'project_type', False),
            ('total click goal', 'total_click_goal', False),
            ('curve type', 'curve_type', False),
            ('links_s3_path', 'links_s3_path', False),
            ('StartDateTimeInclusiveUTC', 'start_date_inclusive_utc', False, datetime_to_wf_format),
            ('EndDateTimeExclusiveUTC', 'end_date_exclusive_utc', False, datetime_to_wf_format),
            ('Click Tier', 'click_tier', False),
            ('Click Tier Value', 'click_tier_value', False),
            ('Open Tier', 'open_tier', False),
            ('Open Tier Value', 'open_tier_value', False),
            ('Overage', 'overage', False),
            ('Campaign Type', 'campaign_type', False),
            ('isCancel', 'is_cancel', False),
            ('Geo Target', 'geo_target', False),
            ('Geo Target State', 'geo_target_state', False, lambda l: l),
        ],
    }

    def __init__(self, prj_name):
        super(WFProjectDisplayContainer, self).__init__(self.template_name, name=prj_name)
