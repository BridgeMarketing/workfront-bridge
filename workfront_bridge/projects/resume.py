from workfront_bridge.blocks.base import WFBlock


class WFProjectResumeContainer(WFBlock):
    '''
    @summary: Workfront Resume Project Container.
    Use this project container to Resume other workfront projects.
    '''

    template_name = "Base Project Container - Resume"

    def __init__(self, prj_name):
        super(WFProjectResumeContainer, self).__init__(self.template_name, name=prj_name)
