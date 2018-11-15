from workfront_bridge.blocks.base import WFBlock


class WFProjectSocialContainer(WFBlock):
    """
    @summary: Workfront Social Project Container.
    Use this project container to create Workfront social projects.
    The container has no preset tasks, but it has the project level fields.
    """

    template_name = "Base Project Container - Social Channel"

    def __init__(self, prj_name):
        super(WFProjectSocialContainer, self).__init__(self.template_name, name=prj_name)
        self._add_optional_parameters([
            "FB/Instagram Audience S3 URI",
        ])
        self._audience_s3_uri = None

    @property
    def audience_s3_uri(self):
        return self._audience_s3_uri

    @audience_s3_uri.setter
    def audience_s3_uri(self, v):
        self._audience_s3_uri = v
        self.set_parameter("", "FB/Instagram Audience S3 URI", v)

