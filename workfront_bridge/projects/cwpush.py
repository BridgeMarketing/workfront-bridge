from workfront_bridge.blocks.base import WFBlock


class CWPushContainer(WFBlock):
    """
    @summary: Workfront CW Push Project Container.
    Use this project container to create workfront CW Push projects.
    This project container has no tasks in it but has all the fields of the
    custom forms that a CW Push project needs.
    """

    template_name = "Base Project Container - CW Push"

    def __init__(self, prj_name):
        super(CWPushContainer, self).__init__(self.template_name, name=prj_name)

        req = ["Bridge_orderID"]
        self._add_required_parameters(req)
        opt = []
        self._add_optional_parameters(opt)

        # Project Container fields:
        self._bridge_order_id = None

    @property
    def bridge_order_id(self):
        return self._bridge_order_id

    @bridge_order_id.setter
    def bridge_order_id(self, v):
        self._bridge_order_id = v
        self.set_parameter("", "Bridge_orderID", v)
