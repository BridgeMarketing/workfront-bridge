from workfront_bridge.blocks.base import WFBlock


class WFSocialCreativeImageBlock(WFBlock):
    """
    @summary: Social Creative Image block
    """

    template_name = 'Block - Social Image'

    block_params = {
        'Create Creative Image': [
            ('Social Advertiser Website URL', 'advertiser_website_url', True),
            ('Social Image S3 URI', 's3_uri', True),
            ('type', 'task_type', False),
            ('Social Title', 'title', False),
            ('Social Creative Message', 'message', False),
            ('Social Description', 'description', False),
            ('FB/Instagram Call to Action', 'fb_call_to_action', False),
        ],
    }
