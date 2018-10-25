from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.tools import datetime_to_wf_format


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
            "Project Type",
            "total click goal",
            "curve type",
            "links",
            "weights",
            "StartDateInclusiveUTC",
            "EndDateExclusiveUTC"
        ])

        self._ttd_audience_id = None
        self._ttd_campaign_id = None
        self._ttd_flight_id = None
        self._ttd_creative_id = None
        self._ttd_advertiser_id = None
        self._is_targeted_bonus_media = None
        self._project_type = None
        self._total_click_goal = None
        self._curve_type = None
        self._links = None
        self._weights = None
        self._start_date_inclusive_utc = None
        self._end_date_exclusive_utc = None

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

    @property
    def total_click_goal(self):
        return self._total_click_goal

    @total_click_goal.setter
    def total_click_goal(self, v):
        self._total_click_goal = v
        self.set_parameter("", "total click goal", v)

    @property
    def curve_type(self):
        return self._curve_type

    @curve_type.setter
    def curve_type(self, v):
        self._curve_type = v
        self.set_parameter("", "curve type", v)

    @property
    def links(self):
        lst = self._links.split(',')
        return lst

    @links.setter
    def links(self, v):
        strv = ','.join(v)
        self._links = strv
        self.set_parameter("", "links", strv)

    @property
    def weights(self):
        lst = self._weights.split(',')
        lst = map(int, lst)
        return lst

    @weights.setter
    def weights(self, v):
        v = map(str, v)
        strv = ','.join(v)
        self._weights = strv
        self.set_parameter("", "weights", strv)

    @property
    def start_date_inclusive_utc(self):
        return self._start_date_inclusive_utc

    @start_date_inclusive_utc.setter
    def start_date_inclusive_utc(self, v):
        self._start_date_inclusive_utc = v
        self.set_parameter("", "StartDateInclusiveUTC", datetime_to_wf_format(v))

    @property
    def end_date_exclusive_utc(self):
        return self._end_date_exclusive_utc

    @end_date_exclusive_utc.setter
    def end_date_exclusive_utc(self, v):
        self._end_date_exclusive_utc = v
        self.set_parameter("", "EndDateExclusiveUTC", datetime_to_wf_format(v))
