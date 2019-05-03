from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.tools import datetime_to_wf_format


class CWPushContainer(WFBlock):
    """
    @summary: Workfront CW Push Project Container.
    Use this project container to create workfront CW Push projects.
    This project container has no tasks in it but has all the fields of the
    custom forms that a CW Push project needs.
    """

    template_name = "Base Project Container - CW Push"

    block_params = {
        '': [
            ('Bridge_orderID', 'bridge_order_id', True),
            ('Partner Name', 'partner_name', True),
            ('Industry', 'industry', True),
            ('Click Tier', 'click_tier', True),
            ('Open Tier', 'open_tier', True),
            ('Name', 'order_name', False),
            ('HTML Link', 'html_link', False),
            ('Banner Link', 'banner_link', False),
            ('Target Volume', 'target_volume', False),
            ('Start Date', 'start_date', False, datetime_to_wf_format),
            ('Overage', 'overage', False),
            ('Target Volume', 'target_volume', False),
            ('Geo Target', 'geo_target', False),
            ('Geo Target State', 'geo_target_state', False, lambda l: l),
            ('Deployment File Link', 'deployment_file_link', False),
            ('Deployment File Segment', 'deployment_file_segment', False),
            ('CW Tool Link', 'cw_tool_link', False),
            ('Duration', 'duration', False),
            ('PURL Processing Enabled', 'purl_processing_enabled', False),
        ],
    }

    def __init__(self, prj_name):
        super(CWPushContainer, self).__init__(self.template_name, name=prj_name)
