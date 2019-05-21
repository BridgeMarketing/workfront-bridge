from workfront_bridge.blocks.video.campaign import WFVideoCampaignBlock
from workfront_bridge.blocks.video.ad_group_create import WFVideoCreateAdGroupBlock
from workfront_bridge.blocks.video.ad_group_creative_upload import WFVideoCreativeUploadBlock
from workfront_bridge.blocks.video.qa_creative import WFVideoCreativeQABlock
from workfront_bridge.blocks.display.launch import WFDisplayLaunchBlock
from workfront_bridge.projects.video import WFProjectVideoContainer
from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.projects.audio_builder import AudioProjectBuilder


class VideoProjectBuilder(AudioProjectBuilder):
    """
    @summary: Video project builder
    """
    def build(self):
        """
        @summary: build the Workfront project.
        @raise WFBrigeException
        @return: WFProject object
        """

        project = self.build_project(WFProjectVideoContainer)
        data_block = self.build_data_block()
        campaign_block = self.build_campaign_block(WFVideoCampaignBlock)
        ad_group_setup_blocks, qa_blocks = self.build_ad_groups(
            WFVideoCreateAdGroupBlock,
            WFVideoCreativeUploadBlock,
            WFVideoCreativeQABlock
        )

        launch_block = WFDisplayLaunchBlock()

        project_blocks = [
            data_block,
            campaign_block,
        ]
        project_blocks.extend(ad_group_setup_blocks)
        project_blocks.extend(qa_blocks)
        project_blocks.append(launch_block)
        [project.append(block) for block in project_blocks]

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)
        return wf_project
