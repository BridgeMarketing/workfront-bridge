from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.projects.display import \
    WFProjectDisplayContainer
from workfront_bridge.blocks.bonus_media.event_loop import \
    EventLoopSetupBlock
from workfront_bridge.blocks.display.ad_group import WFDisplayAdGroupBlock
from workfront_bridge.blocks.display.campaign import WFDisplayCampaignBlock
from workfront_bridge.blocks.display.data import WFDisplayDataBlock
from workfront_bridge.blocks.display.setup_creative_upload import \
    WFDisplayCreativeUploadBlock


class TargetedBonusMediaProjectBuilder(object):
    """
    @summary: Project builder for targeted bonus media projects.
    """

    def __init__(self, wf, project_name):
        """
        @param wf: Workfront service object
        @param project_name: that the created will have.
        """
        self.project_name = project_name
        self.wf = wf

        # project
        self._ttd_advertiser_id = None
        self._project_type = None
        self._total_click_goal = None
        self._curve_type = None
        self._links = None
        self._weights = None
        self._start_date_inclusive_utc = None

        # blocks
        self._budget_in_impressions_pre_calc = None
        self._landing_page_url = None
        self._image_s3_url = None
        self._adg_base_bid_amount = None

    def set_ttd_advertiser_id(self, v):
        self._ttd_advertiser_id = v

    def set_project_type(self, v):
        self._project_type = v

    def set_total_click_goal(self, v):
        self._total_click_goal = v

    def set_curve_type(self, v):
        self._curve_type = v

    def set_links(self, v):
        self._links = v

    def set_weights(self, v):
        self._weights = v

    def set_start_date_inclusive_utc(self, v):
        self._start_date_inclusive_utc = v

    def set_budget_in_impressions_pre_calc(self, v):
        self._budget_in_impressions_pre_calc = v

    def set_landing_page_url(self, v):
        self._landing_page_url = v

    def set_image_s3_url(self, v):
        self._image_s3_url = v

    def set_adg_base_bid_amount(self, v):
        self._adg_base_bid_amount = v

    def build(self):
        """
        @summary: Build the WF project.
        @raise WFBridgeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        """
        # Mocked campaign.
        project = WFProjectDisplayContainer(self.project_name)
        project.ttd_advertiser_id = self._ttd_advertiser_id
        project.project_type = self._project_type
        project.total_click_goal = self._total_click_goal
        project.curve_type = self._curve_type
        project.links = self._links
        project.weights = self._weights
        project.start_date_inclusive_utc = self._start_date_inclusive_utc
        project.is_targeted_bonus_media = "True"
        aud = WFDisplayDataBlock()
        aud.audience_name = '{} audience'.format(self.project_name)
        project.append(aud)
        camp = WFDisplayCampaignBlock()
        camp.campaign_name = '{} campaign'.format(self.project_name)
        camp.budget_in_impressions_pre_calc = \
            self._budget_in_impressions_pre_calc
        project.append(camp)
        setup = WFDisplayCreativeUploadBlock()
        setup.creative_name = '{} creative'.format(self.project_name)
        setup.landing_page_url = self._landing_page_url
        setup.image_s3_url = self._image_s3_url
        project.append(setup)
        adgroup = WFDisplayAdGroupBlock()
        adgroup.ad_group_name = '{} AdGroup'.format(self.project_name)
        adgroup.adg_base_bid_amount = self._adg_base_bid_amount
        project.append(adgroup)
        el = EventLoopSetupBlock()
        project.append(el)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        return wf_project
