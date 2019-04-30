from workfront_bridge.blocks.base import WFBlock


class WFSuppressionGroupBlock(WFBlock):
    """
    @summary: Use this block to group suppression blocks in a data project.
    """

    template_name = 'Block - Data - Suppression Group'


class WFSuppressionBlock(WFBlock):
    """
    @summary: Use this block to add supression taks into a suppression group.
    There is 2 types of suppressions:
    - type : use supression type setter
    - file : use suppression file path and suppression file type
    """

    template_name = 'Block - Data - Suppression'

    block_params = {
        'Suppression': [
            ('Suppression File Path', 'suppression_file_path', False),
            ('Suppression File Type', 'suppression_file_type', False),
            ('suppression type', 'suppression_type', False),
        ],
    }
