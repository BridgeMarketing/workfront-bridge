from workfront_bridge.blocks.base import WFBlock


class WFB2CBlock(WFBlock):
    """
    @summary: Use this block to create an audience fron a count id.
    """

    template_name = 'Block - Data B2C'

    def __init__(self):
        super(WFB2CBlock, self).__init__(self.template_name)

        req = ['Count Id']
        self._add_required_parameters(req)

        self._count_id = None

    @property
    def count_id(self):
        return self._count_id

    @count_id.setter
    def count_id(self, idd):
        self._count_id = idd
        self.set_parameter('Pull Data', 'Count Id', idd)
