from workfront_bridge.blocks.base import WFBlock


class WFProjectUpdateContainer(WFBlock):
    '''
    @summary: Workfront Update Project Container.
    Use this project container to update other workfront projects.
    '''

    template_name = "Base Project Container - Update"

    def __init__(self, prj_name):
        super(WFProjectUpdateContainer, self).__init__(self.template_name, name=prj_name)
