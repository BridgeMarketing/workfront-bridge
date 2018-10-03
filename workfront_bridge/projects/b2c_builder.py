from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.projects.b2c import WFProjectB2CContainer
from workfront_bridge.blocks.data.b2c import WFB2CBlock
from workfront_bridge.exceptions import WFBrigeException


class B2CProjectBuilder(object):
    """
    @summary: Project builder for B2C projects.
    """

    def __init__(self, wf, project_name):
        """
        @param wf: Workfront service object
        @param project_name: that the created will have.
        """
        self.project_name = project_name
        self.wf = wf

        # Project
        self.audience_id = None
        self.audience_file_path = None
        self.data_task_id = None
        self.suppression_task_ids = []

        # Block
        self.count_id = None
        self.suppression_file_path = None

    def set_audience_id(self, audience_id):
        self.audience_id = audience_id
        return self

    def set_audience_file_path(self, audience_file_path):
        self.audience_file_path = audience_file_path
        return self

    def set_data_task_id(self, data_task_id):
        self.data_task_id = data_task_id
        return self

    def set_suppression_task_ids(self, suppression_task_ids):
        self.suppression_task_ids = suppression_task_ids
        return self

    def set_count_id(self, count_id):
        self.count_id = count_id
        return self

    def _check_viability(self):
        if self.count_id is None:
            raise WFBrigeException("{} is required".format("count_id"))

    def set_suppression_file_path(self, suppression_file_path):
        self.suppression_file_path = suppression_file_path
        return self

    def build(self):
        """
        @summary: Build the WF project.
        @raise WFBridgeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        """
        self._check_viability()

        # Project
        project = WFProjectB2CContainer(self.project_name)
        project.audience_id = self.audience_id
        project.audience_file_path = self.audience_file_path
        project.data_task_id = self.data_task_id
        project.suppression_task_ids = self.suppression_task_ids

        # Block
        block = WFB2CBlock()
        block.count_id = self.count_id
        block.suppression_file_path = self.suppression_file_path
        project.append(block)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        return wf_project
