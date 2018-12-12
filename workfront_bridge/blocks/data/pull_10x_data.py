from workfront_bridge.blocks.base import WFBlock


class WFPull10xDataBlock(WFBlock):
    """
    @summary: Use this block for B2C data projects.
    """

    template_name = 'Block - Data 10x - Pull Data'

    def __init__(self):
        super(WFPull10xDataBlock, self).__init__(self.template_name)

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
