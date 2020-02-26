from workfront_bridge.blocks.base import WFBlock


class WFProjectAudioContainer(WFBlock):
    """
    @summary: Workfront Audio Project Container.
    Use this project container to create Workfront audio projects.
    The container has no preset tasks, but it has the project level fields.
    """

    template_name = "Base Project Container - Audio Channel"

    block_params = {
        '': [
            ('Project Type', 'project_type', False),
            ('TTDAdvertiserID', 'ttd_advertiser_id', False),
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
            ('isCancel', 'is_cancel', False),
        ],
    }

    def __init__(self, prj_name):
        super(WFProjectAudioContainer, self).__init__(self.template_name, name=prj_name)
