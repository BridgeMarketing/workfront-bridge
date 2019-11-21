from workfront_bridge.blocks.base import WFBlock


class WFAudienceBlock(WFBlock):
    """
    @summary: Use this block to group count id blocks in a data project.
    """

    template_name = 'Block - Data - Audience'


class WFBridgeAudienceBlock(WFBlock):
    """
    @summary: Use this block to add pull count data tasks into a count id group.
    There is 2 types of suppressions:
    - type : use supression type setter
    - file : use suppression file path and suppression file type
    """

    template_name = 'Block - Data - Bridge Audience Segment'

    block_params = {
        'Pull Data': [
            ('Count Id', 'count_id', True),
            ('Count Type', 'count_type', False),
        ],
    }


class WFClientAudienceBlock(WFBlock):
    """
    @summary: Use this block to add pull count data tasks into a count id group.
    There is 2 types of suppressions:
    - type : use supression type setter
    - file : use suppression file path and suppression file type
    """

    template_name = 'Block - Data - Client Audience Segment'

    block_params = {
        'Create Matched Audience': [
            ('Audience Name', 'audience_name', True),
            ('Audience File Path', 'audience_file_path', True),
            ('Audience Field Identifier', 'audience_identifier', False),
        ],
    }
