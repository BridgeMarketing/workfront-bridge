from workfront_bridge.blocks.base import WFBlock


class WFProjectB2CContainer(WFBlock):
    """
    @summary: Workfront Data B2C Project Container.
    """

    template_name = "Base Project Container - Data B2C"

    def __init__(self, prj_name):
        super(WFProjectB2CContainer, self).__init__(self.template_name,
                                                    name=prj_name)
