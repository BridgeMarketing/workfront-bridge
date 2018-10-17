from workfront_bridge.projects.display import WFProjectDisplayContainer
from workfront_bridge.blocks.display.ad_group import WFDisplayAdGroupBlock
from workfront_bridge.blocks.display.campaign import WFDisplayCampaignBlock
from workfront_bridge.blocks.display.data import WFDisplayDataBlock
from workfront_bridge.blocks.display.launch import WFDisplayLaunchBlock
from workfront_bridge.blocks.display.order_review import WFDisplayOrderReviewBlock
from workfront_bridge.blocks.display.qa import WFDisplayQABlock
from workfront_bridge.blocks.display.setup import WFDisplaySetupBlock
from workfront_bridge.blocks.display.creative_upload import WFDisplayCreativeUploadBlock
from workfront_bridge.blocks.base import WFBlockParser


class DisplayProjectBuilder(object):
    """
    @summary: Display project builder
    """

    def __init__(self, wf, project_name):
        """
        @param wf: Workfront service object
        @param project_name: project name in Workfront
        """
        self.project_name = project_name
        self.wf = wf

    def build(self):
        """
        @summary: build the Workfront project.
        @raise WFBrigeException
        @return: WFProject object
        """
        project = WFProjectDisplayContainer(self.project_name)

        ad_group_block = WFDisplayAdGroupBlock()
        campaign_block = WFDisplayCampaignBlock()
        data_block = WFDisplayDataBlock()
        launch_block = WFDisplayLaunchBlock()
        order_review_block = WFDisplayOrderReviewBlock()
        qa_block = WFDisplayQABlock()
        setup_block = WFDisplaySetupBlock()

        [project.append(block) for block in [
            order_review_block,
            data_block,
            campaign_block,
            setup_block,
            ad_group_block,
            qa_block,
            launch_block,
        ]]

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)
        return wf_project
