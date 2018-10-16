from workfront_bridge.projects.display import WFProjectDisplayContainer
from workfront_bridge.blocks.display.data import WFDisplayDataBlock
from workfront_bridge.blocks.base import WFBlockParser


class DisplayProjectBuilder(object):
    """
    @summary: Display project builder
    """

    def __init__(self, wf, project_name):
        """
        @param wf: Workfront service object
        @param project_name: project name in Workfront
        """

        self.project_name = project_name
        self.wf = wf

    def build(self):
        """
        @summary: build the Workfront project.
        @raise WFBrigeException
        @return: WFProject object
        """
        project = WFProjectDisplayContainer(self.project_name)
        data_block = WFDisplayDataBlock()
        project.append(data_block)
        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)
        return wf_project
