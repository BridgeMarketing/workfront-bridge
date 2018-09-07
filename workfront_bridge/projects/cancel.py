from workfront_bridge.blocks.base import WFBlock


class WFProjectCancelContainer(WFBlock):
    '''
    @summary: Workfront Cancel Project Container.
    Use this project container to cancel other workfront projects.
    '''

    template_name = "Base Project Container - Cancel"

    def __init__(self, prj_name):
        super(WFProjectCancelContainer, self).__init__(self.template_name,
                                                       name=prj_name)
        #self._add_required_parameters([])
        #self._add_optional_parameters([])
