from workfront_bridge.blocks.base import WFBlock


class WFProjectDisplayContainer(WFBlock):
    """
    @summary: Workfront Display Project Container.
    Use this project container to create Workfront display projects.
    The container has no preset tasks, but it has the project level fields.
    """

    template_name = "Base Project Container - Display Channel"

    def __init__(self, prj_name):
        super(WFProjectDisplayContainer, self).__init__(self.template_name, name=prj_name)
