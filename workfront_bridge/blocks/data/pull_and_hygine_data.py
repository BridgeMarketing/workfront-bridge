from workfront_bridge.blocks.base import WFBlock


class WFPullAndHygieneDataBlock(WFBlock):
    """
    @summary: Use this block for B2C data projects.
    """

    template_name = 'Block - Data B2C - Pull and Hygiene Data'

    block_params = {
        'Pull Data': [
            ('Count Id', 'count_id', True),
        ],
    }
