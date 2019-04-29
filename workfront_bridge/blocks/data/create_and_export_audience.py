from workfront_bridge.blocks.base import WFBlock


class WFCreatExportAudienceBlock(WFBlock):
    """
    @summary: Use this block for match and export data projects.
    """

    template_name = 'Block - Match and Export - Create and Export Audience'

    block_params = {
        'Create Matched Audience': [
            ('Audience Name', 'audience_name', True),
            ('Audience File Path', 'audience_file_path', True),
            ('Audience Field Identifier', 'audience_identifier', False),
        ],
    }
