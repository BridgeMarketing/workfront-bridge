from workfront_bridge.projects.social import WFProjectSocialContainer
from workfront_bridge.blocks.social.order_review import WFSocialOrderReviewBlock
from workfront_bridge.blocks.social.audience import WFSocialDataBlock
from workfront_bridge.blocks.social.campaign import WFSocialSetupBlock
from workfront_bridge.blocks.social.creative_image import WFSocialCreativeImageBlock
from workfront_bridge.blocks.social.creative_video import WFSocialCreativeVideoBlock
from workfront_bridge.blocks.social.creative_carousel_ss import WFSocialCreativeCarouselSlideshowBlock
from workfront_bridge.blocks.social.launch import WFSocialLaunchBlock
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.blocks.base import WFBlockParser


class SocialProjectBuilder(object):
    """
    @summary: Social project builder
    """

    def __init__(self, wf, project_name):
        """
        @param wf: Workfront service object
        @param project_name: project name in Workfront
        """
        self.project_name = project_name
        self.wf = wf
        self.creatives = []

    def add_creative(self, **kwargs):
        """Allowed kwargs:
        * creative_name - required
        * creative_size - required
        * image_s3_url - required
        * clickthrough_url - required
        * landing_page_url - required
        * third_party_tags
        * third_party_impression_tracking_url
        * third_party_impression_tracking_url2
        * third_party_impression_tracking_url3
        * securable
        * availability
        * third_party_tag
        * width
        * height
        """
        pass

    def build(self):
        """
        @summary: build the Workfront project.
        @raise WFBrigeException
        @return: WFProject object
        """
        # if not self.creatives:
        #     raise WFBrigeException('The project does not have any creatives. Please use add_creative to add them.')

        project = WFProjectSocialContainer(self.project_name)
        # Blocks
        order_review_block = WFSocialOrderReviewBlock()
        data_block = WFSocialDataBlock()
        setup_block = WFSocialSetupBlock()
        creative_image_block_1 = WFSocialCreativeImageBlock()
        creative_image_block_2 = WFSocialCreativeImageBlock()
        creative_image_block_3 = WFSocialCreativeImageBlock()
        launch_block = WFSocialLaunchBlock()
        project_blocks = [
            order_review_block,
            data_block,
            setup_block,
            creative_image_block_1,
            creative_image_block_2,
            creative_image_block_3,
            launch_block,
        ]
        [project.append(block) for block in project_blocks]
        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)
        return wf_project
