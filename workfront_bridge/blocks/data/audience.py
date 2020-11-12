from workfront_bridge.blocks.base import WFBlock


class WFAudienceBlock(WFBlock):
    """
    @summary: Use this block to group count id blocks in a data project.
    """

    template_name = "Block - Data - Audience"


class WFBridgeAudienceBlock(WFBlock):
    """
    @summary: Use this block to add pull count data tasks into a count id group.
    There is 2 types of suppressions:
    - type : use supression type setter
    - file : use suppression file path and suppression file type
    """

    template_name = "Block - Data - Bridge Audience Segment"

    block_params = {
        "Bridge Audience Segment": [
            ("Count Id", "count_id", True),
            ("Count Type", "count_type", False),
        ],
    }


class WFClientAudienceBlock(WFBlock):
    """
    @summary: Use this block to add pull count data tasks into a count id group.
    There is 2 types of suppressions:
    - type : use supression type setter
    - file : use suppression file path and suppression file type
    """

    template_name = "Block - Data - Client Audience Segment"

    block_params = {
        "Client Audience Segment": [
            ("Audience Name", "audience_name", True),
            ("Audience File Path", "audience_file_path", True),
            ("Audience Field Identifier", "audience_identifier", False),
            ("Audience Field Map", "audience_field_map", False),
        ],
    }


class WFInstallAudienceBlock(WFBlock):
    """
    @summary: Use this block to add pull count data tasks into a count id group.
    There is 2 types of suppressions:
    - type : use supression type setter
    - file : use suppression file path and suppression file type
    """

    template_name = "Block - Data - Install Audience Segment"

    block_params = {
        "Install Audience Segment": [
            ("Audience Name", "audience_name", True),
            ("Audience File Path", "audience_file_path", True),
            ("Audience Field Identifier", "audience_identifier", False),
            ("Audience Field Map", "audience_field_map", False),
            ("Audience Segment Type", "segment_type", True),
            ("install_tables", "install_tables", True),
            ("install_columns", "install_columns", True),
        ],
    }


class WFRetrieveProviderParamsFromDWH(WFBlock):
    """
    @summary: Use this block to retrieve retargeting audience.
    """

    template_name = "Block - Data - Retrieve Provider Params From DWH"
    block_params = {
        "Retrieve Provider Params From DWH": [
            ("Parent WF Project ID", "parent_wf_project_id", True),
        ],
    }


class WFRetrieveRetargetingAudience(WFBlock):
    """
    @summary: Use this block to retrieve retargeting audience.
    """

    template_name = "Block - Data - Retrieve Retargeting Audience"
    block_params = {
        "Retrieve Retargeting Audience": [
            ("Retargeting Type", "retargeting_type", False),
        ],
    }
