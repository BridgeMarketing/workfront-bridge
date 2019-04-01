from workfront_bridge.blocks.base import WFBlock


class WFProjectAudioContainer(WFBlock):
    """
    @summary: Workfront Audio Project Container.
    Use this project container to create Workfront audio projects.
    The container has no preset tasks, but it has the project level fields.
    """

    template_name = "Base Project Container - Audio Channel"

    def __init__(self, prj_name):
        super(WFProjectAudioContainer, self).__init__(self.template_name, name=prj_name)
        self._add_optional_parameters([
            'Project Type',
        ])
        self._project_type = 'Audio'
        self.set_parameter('', 'Project Type', 'Audio')
