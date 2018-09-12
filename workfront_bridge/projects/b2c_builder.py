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

        # Block
        self.count_id = None

    def set_count_id(self, count_id):
        self.count_id = count_id
        return self

    def _check_viability(self):
        if self.count_id is None:
            raise WFBrigeException("{} is required".format("count_id"))

    def build(self):
        """
        @summary: Build the WF project.
        @raise WFBridgeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        """
        self._check_viability()

        project = WFProjectB2CContainer(self.project_name)

        # Block
        block = WFB2CBlock()
        block.count_id = self.count_id
        project.append(block)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        return wf_project
