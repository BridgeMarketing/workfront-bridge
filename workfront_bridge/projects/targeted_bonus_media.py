from workfront_bridge.blocks.base import WFBlock


class WFProjectTargetedBonusMediaContainer(WFBlock):
    """
    @summary: Workfront TBM Project Container.
    """

    template_name = "Base Project Container - Targeted Bonus Media Channel"

    def __init__(self, prj_name):
        super(WFProjectTargetedBonusMediaContainer, self).__init__(
            self.template_name,
            name=prj_name)

        opt = []
        self._add_optional_parameters(opt)

        # Project Container fields:
        # self._dummy = None

    # @property
    # def audience_id(self):
    #     return self._audience_id

    # @audience_id.setter
    # def audience_id(self, v):
    #     self._audience_id = v
    #     self.set_parameter("", "Audience Id", v)
