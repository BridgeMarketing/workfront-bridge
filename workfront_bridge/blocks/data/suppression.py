from workfront_bridge.blocks.base import WFBlock


class WFSuppressionGroupBlock(WFBlock):
    """
    @summary: Use this block to group suppression blocks in a data project.
    """

    template_name = 'Block - Data - Suppression Group'

    def __init__(self):
        super(WFSuppressionGroupBlock, self).__init__(self.template_name)


class WFSuppressionBlock(WFBlock):
    """
    @summary: Use this block to add supression taks into a suppression group.
    There is 2 types of suppressions:
    - type : use supression type setter
    - file : use suppression file path and suppression file type
    """

    template_name = 'Block - Data - Suppression'

    def __init__(self):
        super(WFSuppressionBlock, self).__init__(self.template_name)

        optional_parameters = [
            'Suppression File Path',
            'Suppression File Type',
            'suppression type'
        ]
        self._add_optional_parameters(optional_parameters)

        self._suppression_file_path = None
        self._suppression_file_type = None

        self._suppression_type = None

    @property
    def suppression_file_path(self):
        return self._suppression_file_path

    @suppression_file_path.setter
    def suppression_file_path(self, sup_file_path):
        self._suppression_file_path = sup_file_path
        self.set_parameter('Suppression',
                           'Suppression File Path',
                           self._suppression_file_path)

    @property
    def suppression_file_type(self):
        return self._suppression_file_type

    @suppression_file_type.setter
    def suppression_file_type(self, sup_file_type):
        self._suppression_file_type = sup_file_type
        self.set_parameter('Suppression',
                           'Suppression File Type',
                           self._suppression_file_type)

    @property
    def suppression_type(self):
        return self._suppression_type

    @suppression_type.setter
    def suppression_type(self, sup_type):
        self._suppression_type = sup_type
        self.set_parameter('Suppression', 'suppression type', sup_type)
