from workfront_bridge.blocks.base import WFBlock


class WFCountIdGroupBlock(WFBlock):
    """
    @summary: Use this block to group count id blocks in a data project.
    """

    template_name = 'Block - Data - Count Id'


class WFCountIdBlock(WFBlock):
    """
    @summary: Use this block to add pull count data tasks into a count id group.
    There is 2 types of suppressions:
    - type : use supression type setter
    - file : use suppression file path and suppression file type
    """

    template_name = 'Block - Data - Count Id'

    block_params = {
        'Pull Data': [
            ('Count Id', 'count_id', True),
            ('Count Type', 'count_type', False),
        ],
    }
