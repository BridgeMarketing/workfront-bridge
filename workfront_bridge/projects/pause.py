from workfront_bridge.blocks.base import WFBlock


class WFProjectPauseContainer(WFBlock):
    '''
    @summary: Workfront Pause Project Container.
    Use this project container to pause other workfront projects.
    '''

    template_name = "Base Project Container - Pause"

    def __init__(self, prj_name):
        super(WFProjectPauseContainer, self).__init__(self.template_name,
                                                       name=prj_name)

