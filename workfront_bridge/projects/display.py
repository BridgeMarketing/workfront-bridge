from workfront_bridge.blocks.base import WFBlock


class WFProjectDisplayContainer(WFBlock):
    """
    @summary: Workfront Display Project Container.
    Use this project container to create Workfront display projects.
    The container has no preset tasks, but it has the project level fields.
    """

    template_name = "Base Project Container - Display Channel"

    def __init__(self, prj_name):
        super(WFProjectDisplayContainer, self).__init__(self.template_name, name=prj_name)

        self._add_required_parameters([
            "TTDAdvertiserID",
        ])
        self._add_optional_parameters([
            "TTDAudienceID",
            "TTDCampaignID",
            "TTDFlightID",
            "TTDCreativeID",
            "IsTargetedBonusMedia",
            "Project Type"
        ])

        self._ttd_audience_id = None
        self._ttd_campaign_id = None
        self._ttd_flight_id = None
        self._ttd_creative_id = None
        self._ttd_advertiser_id = None
        self._is_targeted_bonus_media = None
        self._project_type = None

    @property
    def ttd_audience_id(self):
        return self._ttd_audience_id

    @ttd_audience_id.setter
    def ttd_audience_id(self, v):
        self._ttd_audience_id = v
        self.set_parameter("", "TTDAudienceID", v)

    @property
    def ttd_campaign_id(self):
        return self._ttd_campaign_id

    @ttd_campaign_id.setter
    def ttd_campaign_id(self, v):
        self._ttd_campaign_id = v
        self.set_parameter("", "TTDCampaignID", v)

    @property
    def ttd_flight_id(self):
        return self._ttd_flight_id

    @ttd_flight_id.setter
    def ttd_flight_id(self, v):
        self._ttd_flight_id = v
        self.set_parameter("", "TTDFlightID", v)

    @property
    def ttd_creative_id(self):
        return self._ttd_creative_id

    @ttd_creative_id.setter
    def ttd_creative_id(self, v):
        self._ttd_creative_id = v
        self.set_parameter("", "TTDCreativeID", v)

    @property
    def ttd_advertiser_id(self):
        return self._ttd_advertiser_id

    @ttd_advertiser_id.setter
    def ttd_advertiser_id(self, v):
        self._ttd_advertiser_id = v
        self.set_parameter("", "TTDAdvertiserID", v)

    @property
    def is_targeted_bonus_media(self):
        return self._is_targeted_bonus_media

    @is_targeted_bonus_media.setter
    def is_targeted_bonus_media(self, v):
        self._is_targeted_bonus_media = v
        self.set_parameter("", "IsTargetedBonusMedia", v)

    @property
    def project_type(self):
        return self._project_type

    @project_type.setter
    def project_type(self, v):
        self._project_type = v
        self.set_parameter("", "Project Type", v)



