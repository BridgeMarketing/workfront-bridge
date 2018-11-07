from workfront_bridge.projects.social import WFProjectSocialContainer
from workfront_bridge.blocks.social.order_review import WFSocialOrderReviewBlock
from workfront_bridge.blocks.social.audience import WFSocialDataBlock
from workfront_bridge.blocks.social.campaign import WFSocialSetupBlock
from workfront_bridge.blocks.social.ad_group_setup import WFSocialAdGroupSetupBlock
from workfront_bridge.blocks.social.launch import WFSocialLaunchBlock
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.blocks.base import WFBlockParser


class SocialProjectBuilder(object):
    """
    @summary: Social project builder
    """
    ad_group_fields = [
        'bid_amount',
        'impressions_or_clicks',
        'number_of_impressions',
        'budget_daily_or_lifetime',
        'datetime_start',
        'datetime_end',
        'device_type',
        'mobile_os',
        'exclude_categories',
        'creatives',    # Nested
    ]

    creative_common_fields = [
        'creative_type',
        'message',
        'advertiser_website_url',
        'fb_call_to_action',
        'fb_facebook_platforms',
        'fb_instagram_platforms',
        'fb_facebook_page_id',
        'fb_instagram_account_id',
        'fb_audience_network_platforms',
        'fb_instagram_messenger_platforms',
    ]

    creative_image_fields = [
        's3_uri',
        'title',
        'description',
    ]

    creative_video_fields = [
        's3_uri',
        'image_s3_uri',
        'title',
        'description',
    ]

    creative_carousel_or_slideshow_fields = [
        'carousel_or_slideshow',
        'creatives'
    ]

    def __init__(self, wf, project_name):
        """
        @param wf: Workfront service object
        @param project_name: project name in Workfront
        """
        self.project_name = project_name
        self.wf = wf
        self._ad_groups = []

        self.creative_type_allowed_fields = {
            'image': self.creative_image_fields + self.creative_common_fields,
            'video': self.creative_video_fields + self.creative_common_fields,
            'carousel/slideshow': self.creative_carousel_or_slideshow_fields + self.creative_common_fields,
        }

        # Setup block
        self._campaign_title = None
        self._fb_page_id = None
        self._fb_ig_acc_id = None
        self._fb_advertising_objective = None
        self._fb_offer = None
        self._fb_apply_block_list = None

        # Launch block
        self._provider = None

    def add_ad_group(self, ad_group):
        """
        Ad Group kwargs:
        {}
        
        Creative common kwargs:
        {}
        """.format(self.ad_group_fields, self.creative_common_fields)
        allowed_keys = self.ad_group_fields
        for k, v in ad_group.items():
            if k not in allowed_keys:
                raise WFBrigeException('Invalid Key {}'.format(k))
            elif k == 'creatives':
                for creative in v:
                    creative_allowed_keys = self.creative_type_allowed_fields[creative['creative_type']]
                    for creative_key, creative_value in creative.items():
                        if creative_key not in creative_allowed_keys:
                            raise WFBrigeException('Invalid Key {}'.format(k))
        self._ad_groups.append(ad_group)

    def build(self):
        """
        @summary: build the Workfront project.
        @raise WFBrigeException
        @return: WFProject object
        """
        if not self._ad_groups:
            raise WFBrigeException('The project does not have any ad_groups. Please use add_ad_group to add them.')

        project = WFProjectSocialContainer(self.project_name)

        # Blocks
        order_review_block = WFSocialOrderReviewBlock()
        data_block = WFSocialDataBlock()

        setup_block = WFSocialSetupBlock()
        setup_block.campaign_title = self._campaign_title
        setup_block.fb_page_id = self._fb_page_id
        setup_block.fb_ig_acc_id = self._fb_ig_acc_id
        setup_block.fb_advertising_objective = self._fb_advertising_objective
        setup_block.fb_offer = self._fb_offer
        setup_block.fb_apply_block_list = self._fb_apply_block_list

        ad_group_setup_blocks = []
        for ad_group in self._ad_groups:
            ad_group_setup_block = WFSocialAdGroupSetupBlock()
            for creative in ad_group['creatives']:
                creative_upload_dict = {k: creative[k] for k
                                        in self.creative_type_allowed_fields[creative['creative_type']]
                                        if k in creative}
                ad_group_setup_block.add_creative(**creative_upload_dict)
            ad_group_setup_block.add_ad_group(**ad_group)
            ad_group_setup_blocks.append(ad_group_setup_block)

        launch_block = WFSocialLaunchBlock()
        launch_block.provider = self._provider

        project_blocks = [
            order_review_block,
            data_block,
            setup_block
        ]
        project_blocks.extend(ad_group_setup_blocks)
        project_blocks.append(launch_block)

        [project.append(block) for block in project_blocks]
        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)
        return wf_project

    # For Pablo
    def set_campaign_title(self, v):
        self._campaign_title = v
        return self

    def set_fb_page_id(self, v):
        self._fb_page_id = v
        return self

    def set_fb_ig_acc_id(self, v):
        self._fb_ig_acc_id = v
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
