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
import datetime


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

    def build(self):
        """
        @summary: Build the WF project.
        @raise WFBridgeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        """
        project = WFProjectDisplayContainer(self.project_name)
        project.ttd_advertiser_id = "xc7votu"
        project.project_type = "Display - Desktop & Mobile"
        project.total_click_goal = 20
        project.curve_type = 1
        project.links = "https://k0ch.github.io/,https://k0ch.github.io/peppe"
        project.weights = "50,50"
        project.start_date_inclusive_utc = datetime.datetime.strptime('28102018', "%d%m%Y").date()
        project.end_date_exclusive_utc = datetime.datetime.strptime('30102018', "%d%m%Y").date()
        aud = WFDisplayDataBlock()
        aud.audience_name = "TBM audience"
        project.append(aud)
        camp = WFDisplayCampaignBlock()
        camp.start_date_inclusive_utc = datetime.datetime.strptime('28102018', "%d%m%Y").date()
        camp.end_date_exclusive_utc = datetime.datetime.strptime('30102018', "%d%m%Y").date()
        camp.campaign_name = "TBM campaign"
        camp.budget_in_impressions_pre_calc = 80000
        project.append(camp)
        setup = WFDisplayCreativeUploadBlock()
        setup.creative_name = 'TBM creative'
        setup.clickthrough_url = 'Test Clickthrough URL 3'
        setup.landing_page_url = 'Test Landing Page URL 3'
        setup.image_s3_url = 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/mobile_banner.png'
        project.append(setup)
        adgroup = WFDisplayAdGroupBlock()
        adgroup.ad_group_name = "TBM AdGroup"
        adgroup.adg_base_bid_amount = 1.5
        project.append(adgroup)
        el = EventLoopSetupBlock()
        project.append(el)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        return wf_project
