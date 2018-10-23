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
    creative_common_fields = [
        "creative_type",
        "message",
        "advertiser_website_url",
        "fb_call_to_action",
        "fb_facebook_platforms",
        "fb_instagram_platforms",
        "fb_facebook_page_id",
        "fb_instagram_account_id",
        "fb_audience_network_platforms",
        "fb_instagram_messenger_platforms",
    ]

    creative_image_fields = [
        "s3_uri",
        "title",
        "description",
    ]

    creative_video_fields = [
        "s3_uri",
        "image_s3_uri",
        "title",
        "description",
    ]

    creative_carousel_or_slideshow_fields = [
        "carousel_or_slideshow",
        "creatives"
    ]

    def __init__(self, wf, project_name):
        """
        @param wf: Workfront service object
        @param project_name: project name in Workfront
        """
        self.project_name = project_name
        self.wf = wf
        self._creatives = []

        # Setup block
        self._campaign_title = None
        self._bid_amount = None
        self._impressions_or_clicks = None
        self._number_of_impressions = None
        self._budget_daily_or_lifetime = None
        self._datetime_start = None
        self._datetime_end = None
        self._device_type = None
        self._mobile_os = None
        self._exclude_categories = None
        self._fb_advertising_objective = None
        self._fb_offer = None
        self._fb_apply_block_list = None

        # Launch block
        self._provider = None

    def add_creative(self, **kwargs):
        """Allowed kwargs:
        * creative_type - required
        * message - required
        * advertiser_website_url - required
        * fb_call_to_action
        * fb_facebook_platforms
        * fb_instagram_platforms
        """
        type_to_fields = {
            'image': self.creative_image_fields,
            'video': self.creative_video_fields,
            'carousel/slideshow': self.creative_carousel_or_slideshow_fields,
        }
        allowed_fields = self.creative_common_fields + type_to_fields[kwargs['creative_type']]
        creative = {}
        for k, v in kwargs.items():
            if k not in allowed_fields:
                raise WFBrigeException('Invalid keyword argument {} for creative {}. Allowed fields: {}'
                                       .format(k, kwargs['creative_type'], allowed_fields))
            creative[k] = v
            # TODO: validate carousel assets
        self._creatives.append(creative)

    def build(self):
        """
        @summary: build the Workfront project.
        @raise WFBrigeException
        @return: WFProject object
        """
        if not self._creatives:
            raise WFBrigeException('The project does not have any creatives. Please use add_creative to add them.')

        project = WFProjectSocialContainer(self.project_name)

        # Blocks
        order_review_block = WFSocialOrderReviewBlock()

        data_block = WFSocialDataBlock()

        setup_block = WFSocialSetupBlock()
        setup_block.campaign_title = self._campaign_title
        setup_block.bid_amount = self._bid_amount
        setup_block.impressions_or_clicks = self._impressions_or_clicks
        setup_block.number_of_impressions = self._number_of_impressions
        setup_block.budget_daily_or_lifetime = self._budget_daily_or_lifetime
        setup_block.datetime_start = self._datetime_start
        setup_block.datetime_end = self._datetime_end
        setup_block.device_type = self._device_type
        setup_block.mobile_os = self._mobile_os
        setup_block.exclude_categories = self._exclude_categories
        setup_block.fb_advertising_objective = self._fb_advertising_objective
        setup_block.fb_offer = self._fb_offer
        setup_block.fb_apply_block_list = self._fb_apply_block_list

        creative_blocks = []
        for creative in self._creatives:
            type_to_class = {
                'image': WFSocialCreativeImageBlock,
                'video': WFSocialCreativeVideoBlock,
                'carousel/slideshow': WFSocialCreativeCarouselSlideshowBlock,
            }
            CreativeBlockClass = type_to_class[creative['creative_type']]
            creative_block = CreativeBlockClass()
            for k, v in creative.items():
                if k == 'creatives':
                    # For carousels, add 'sub-creatives' (images and videos), also called assets
                    for c in v:
                        creative_block.add_creative(c)
                elif k != 'creative_type':
                    setattr(creative_block, k, v)

            creative_blocks.append(creative_block)

        launch_block = WFSocialLaunchBlock()
        launch_block.provider = self._provider

        project_blocks = [
            order_review_block,
            data_block,
            setup_block
        ]
        project_blocks.extend(creative_blocks)
        project_blocks.append(launch_block)

        [project.append(block) for block in project_blocks]
        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)
        return wf_project

    # For Pablo
    def set_campaign_title(self, v):
        self._campaign_title = v
        return self

    def set_bid_amount(self, v):
        self._bid_amount = v
        return self

    def set_impressions_or_clicks(self, v):
        self._impressions_or_clicks = v
        return self

    def set_number_of_impressions(self, v):
        self._number_of_impressions = v
        return self

    def set_budget_daily_or_lifetime(self, v):
        self._budget_daily_or_lifetime = v
        return self

    def set_datetime_start(self, v):
        self._datetime_start = v
        return self

    def set_datetime_end(self, v):
        self._datetime_end = v
        return self

    def set_device_type(self, v):
        self._device_type = v
        return self

    def set_mobile_os(self, v):
        self._mobile_os = v
        return self

    def set_exclude_categories(self, v):
        self._exclude_categories = v
        return self

    def set_fb_advertising_objective(self, v):
        self._fb_advertising_objective = v
        return self

    def set_fb_offer(self, v):
        self._fb_offer = v
        return self

    def set_fb_apply_block_list(self, v):
        self._fb_apply_block_list = v
        return self

    def set_provider(self, v):
        self._provider = v
        return self

