from workfront_bridge.blocks.base import WFBlock


class WFProjectSocialContainer(WFBlock):
    """
    @summary: Workfront Social Project Container.
    Use this project container to create Workfront social projects.
    The container has no preset tasks, but it has the project level fields.
    """

    template_name = "Base Project Container - Display Channel"

    def __init__(self, prj_name):
        super(WFProjectSocialContainer, self).__init__(self.template_name, name=prj_name)
