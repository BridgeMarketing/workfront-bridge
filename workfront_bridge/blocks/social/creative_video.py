from workfront_bridge.blocks.base import WFBlock


class WFSocialCreativeVideoBlock(WFBlock):
    """
    @summary: Social Creative Video block
    """

    template_name = 'Block - Social Video'

    block_params = {
        'Create Creative Video': [
            ('Social Creative Message', 'message', True),
            ('Social Advertiser Website URL', 'advertiser_website_url', True),
            ('Social Video S3 URI', 's3_uri', True),
            ('Social Video Image S3 URI', 'image_s3_uri', True),
            ('type', 'task_type', False),
            ('Social Title', 'title', False),
            ('FB/Instagram Call to Action', 'fb_call_to_action', False),
        ],
    }
