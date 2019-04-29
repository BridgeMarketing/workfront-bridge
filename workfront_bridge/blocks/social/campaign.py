from workfront_bridge.blocks.base import WFBlock


class WFSocialSetupBlock(WFBlock):
    """
    @summary: Social Setup block. Campaign information.
    """

    template_name = 'Block - Social Setup'

    block_params = {
        'Create Campaign': [
            ('Social Campaign Title', 'campaign_title', True),
            ('FB/Instagram FB Page ID', 'fb_page_id', False),
            ('FB/Instagram IG Account ID', 'fb_ig_acc_id', False),
            ('FB/Instagram Advertising Objective', 'fb_advertising_objective', False),
            ('FB/Instagram Offer', 'fb_offer', False),
            ('FB/Instagram Apply Block List', 'fb_apply_block_list', False),
        ],
    }
