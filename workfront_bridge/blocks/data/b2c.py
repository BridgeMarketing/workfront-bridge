from workfront_bridge.blocks.base import WFBlock


class WFB2CBlock(WFBlock):
    """
    @summary: Use this block to create an audience fron a count id.
    """

    template_name = 'Block - Data B2C v2'

    def __init__(self):
        super(WFB2CBlock, self).__init__(self.template_name)

        req = ['Count Id']
        optional_parameters = ['Suppression File Path', 'suppression type']

        self._count_id = None
        self._suppression_file_path = None

        self._add_required_parameters(req)
        self._add_optional_parameters(optional_parameters)

    @property
    def count_id(self):
        return self._count_id

    @count_id.setter
    def count_id(self, idd):
        self._count_id = idd
        self.set_parameter('Pull Data', 'Count Id', idd)

    @property
    def suppression_file_path(self):
        return self._suppression_file_path

    @suppression_file_path.setter
    def suppression_file_path(self, sup_file_path):
        self._suppression_file_path = sup_file_path
        self.set_parameter(
            'Suppression',
            'Suppression File Path',
            sup_file_path)

    @property
    def suppression_type(self):
        return self._suppression_type

    @suppression_type.setter
    def suppression_type(self, sup_type):
        self._suppression_type = sup_type
        self.set_parameter('Suppression', 'suppression type', sup_type)
