from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.projects.targeted_bonus_media import \
    WFProjectTargetedBonusMediaContainer
from workfront_bridge.blocks.bonus_media.targeted import  \
    TargetedBonusMediaBlock


class TargetedBonusMediaProjectBuilder(object):
    """
    @summary: Project builder for targeted bonus media projects.
    """

    def __init__(self, wf, project_name):
        """
        @param wf: Workfront service object
        @param project_name: that the created will have.
        """
        self.project_name = project_name
        self.wf = wf

    def build(self):
        """
        @summary: Build the WF project.
        @raise WFBridgeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        """
        project = WFProjectTargetedBonusMediaContainer(self.project_name)
        block = TargetedBonusMediaBlock()
        project.append(block)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        return wf_project
