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
        # Block
        block = CWPushBlock()
        project.append(block)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)
        return wf_project
