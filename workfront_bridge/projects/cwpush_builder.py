from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.projects.cwpush import CWPushContainer
from workfront_bridge.blocks.cwtool.cwpush import CWPushBlock


class CWToolProjectBuilder(object):
    """
    @summary: Project builder for CW Push projects.
    """

    def __init__(self, wf, project_name):
        """
        @param wf: Workfront service object
        @param project_name: that the created will have.
        """
        self.project_name = project_name
        self.wf = wf

        # Project
        self.bridge_order_id = None
        self.order_name = None
        self.partner_name = None
        self.industry = None
        self.html_link = None
        self.banner_link = None
        self.start_date = None
        self.target_volume = None
        self.overage = None
        self.geo_target = None
        self.geo_target_state = None
        self.deployment_file_link = None
        self.deployment_file_segment = None
        self.click_tier = None
        self.open_tier = None
        self.cw_tool_link = None

    def build(self):
        """
        @summary: Build the WF project.
        @raise WFBridgeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        """
        project = CWPushContainer(self.project_name)
        # Project
        project.bridge_order_id = self.bridge_order_id
        project.order_name = self.order_name
        project.partner_name = self.partner_name
        project.industry = self.industry
        project.html_link = self.html_link
        project.banner_link = self.banner_link
        project.start_date = self.start_date
        project.target_volume = self.target_volume
        project.overage = self.overage
        project.geo_target = self.geo_target
        project.geo_target_state = self.geo_target_state
        project.deployment_file_link = self.deployment_file_link
        project.deployment_file_segment = self.deployment_file_segment
        project.click_tier = self.click_tier
        project.open_tier = self.open_tier
        project.cw_tool_link = self.cw_tool_link
        # Block
        block = CWPushBlock()
        project.append(block)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)
        return wf_project
