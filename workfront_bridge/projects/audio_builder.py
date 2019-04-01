from workfront_bridge.projects.audio import WFProjectAudioContainer
from workfront_bridge.blocks.base import WFBlockParser


class AudioProjectBuilder(object):
    """
    @summary: Audio project builder
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

        project = WFProjectAudioContainer(self.project_name)

        project_blocks = [
        ]

        [project.append(block) for block in project_blocks]
        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)
        return wf_project
