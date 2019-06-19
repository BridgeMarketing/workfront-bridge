from workfront_bridge.blocks.base import WFBlock


class WFPull10xDataBlock(WFBlock):
    """
    @summary: Use this block for B2C data projects.
    """

    template_name = 'Block - Data 10x - Pull Data'

    block_params = {
        'Pull Data': [
            ('Count Id', 'count_id', True),
            ('Count Type', 'count_type', False),
        ],
    }
