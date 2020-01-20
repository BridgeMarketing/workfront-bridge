from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.projects.display import \
    WFProjectDisplayContainer
from workfront_bridge.blocks.bonus_media.event_loop import \
    EventLoopSetupBlock
from workfront_bridge.blocks.display.ad_group_setup import WFDisplayAdGroupSetupBlock
from workfront_bridge.blocks.display.campaign import WFDisplayCampaignBlock
from workfront_bridge.blocks.display.data import WFDisplayDataBlock


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
        self._ttd_bonus_media_advertiser_id = None
        self._lr_account_id = None
        self._lr_bonus_media_account_id = None
        self._project_type = None
        self._total_click_goal = None
        self._curve_type = None
        self._links = None
        self._weights = None
        self._links_ids = None
        self._start_date_inclusive_utc = None
        self._open_tier = None
        self._open_tier_value = None
        self._click_tier = None
        self._click_tier_value = None
        self._overage = False
        self._campaign_type = None

        # blocks
        self._budget_in_impressions_pre_calc = None
        self._landing_page_url = None
        self._image_s3_url = None
        self._adg_base_bid_amount = None
        self._adg_max_bid_amount = None

        self._ad_group_name = None
        self._campaign_name = None

    def set_campaign_name(self, name):
        self._campaign_name = name

    def set_ad_group_name(self, name):
        self._ad_group_name = name

    def set_open_tier(self, v):
        self._open_tier = v

    def set_open_tier_value(self, v):
        self._open_tier_value = v

    def set_click_tier(self, v):
        self._click_tier = v

    def set_click_tier_value(self, v):
        self._click_tier_value = v

    def set_overage(self, v):
        self._overage = v

    def set_campaign_type(self, v):
        self._campaign_type = v

    def set_ttd_advertiser_id(self, v):
        self._ttd_advertiser_id = v
        return self

    def set_ttd_bonus_media_advertiser_id(self, v):
        self._ttd_bonus_media_advertiser_id = v
        return self

    def set_lr_account_id(self, v):
        self._lr_account_id = v 
        return self

    def set_lr_bonus_media_account_id(self, v):
        self._lr_bonus_media_account_id = v 
        return self

    def set_project_type(self, v):
        self._project_type = v

    def set_total_click_goal(self, v):
        self._total_click_goal = v

    def set_curve_type(self, v):
        self._curve_type = v

    def set_links(self, v):
        self._links = v

    def set_links_ids(self, v):
        self._links_ids = v

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

    def set_adg_max_bid_amount(self, v):
        self._adg_max_bid_amount = v

    def build(self):
        """
        @summary: Build the WF project.
        @raise WFBridgeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        """
        project = WFProjectDisplayContainer(self.project_name)
        project.lr_bonus_media_account_id = self._lr_bonus_media_account_id
        project.lr_account_id = self._lr_account_id
        project.ttd_advertiser_id = self._ttd_advertiser_id
        project.ttd_bonus_media_advertiser_id = self._ttd_bonus_media_advertiser_id

        project.project_type = self._project_type
        project.total_click_goal = self._total_click_goal
        project.curve_type = self._curve_type
        project.links = self._links
        project.weights = self._weights
        project.links_ids = self._links_ids
        project.start_date_inclusive_utc = self._start_date_inclusive_utc
        project.is_targeted_bonus_media = "True"
        project.click_tier = self._click_tier
        project.click_tier_value = self._click_tier_value
        project.open_tier = self._open_tier
        project.open_tier_value = self._open_tier_value
        project.overage = self._overage
        project.campaign_type = self._campaign_type

        aud = WFDisplayDataBlock()
        aud.audience_name = '{} audience'.format(self.project_name)
        project.append(aud)
        camp = WFDisplayCampaignBlock()
        camp.campaign_name = self._campaign_name or '{} campaign'.format(self.project_name)
        camp.budget_in_impressions_pre_calc = \
            self._budget_in_impressions_pre_calc
        project.append(camp)

        ad_group_setup_block = WFDisplayAdGroupSetupBlock()
        ad_group_setup_block.add_creative(
            creative_type='Image Banner or Interstitial',
            creative_name='{} creative'.format(self.project_name),
            landing_page_url=self._landing_page_url,
            image_s3_url=self._image_s3_url,
        )

        ag_name = self._ad_group_name or '{} AdGroup'.format(self.project_name)

        ad_group_setup_block.add_ad_group(
            ad_group_name=ag_name,
            adg_base_bid_amount=self._adg_base_bid_amount,
            adg_max_bid_amount=self._adg_max_bid_amount
        )
        project.append(ad_group_setup_block)

        el = EventLoopSetupBlock()
        project.append(el)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        return wf_project
