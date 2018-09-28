from workfront_bridge.blocks.base import WFBlock


class WFMatchAndExport1ABlock(WFBlock):
    """
    @summary: Use this block to create an audience
    """

    template_name = 'Block - Match and Export 1A'

    def __init__(self):
        super(WFMatchAndExport1ABlock, self).__init__(self.template_name)

        req = [
            'Audience Name',
            'Audience File Path'
        ]

        optional_parameters = ["Audience Field Identifier", "Suppression File Path"]

        self._audience_name = None
        self._audience_file_path = None
        self._suppression_file_path = None
        self._audience_identifier = "oneAudienceID"

        self._add_required_parameters(req)
        self._add_optional_parameters(optional_parameters)

    @property
    def audience_name(self):
        return self._audience_name

    @audience_name.setter
    def audience_name(self, name):
        self._audience_name = name
        self.set_parameter('Create Matched Audience', 'Audience Name', name)

    @property
    def audience_file_path(self):
        return self._audience_file_path

    @audience_file_path.setter
    def audience_file_path(self, file_path):
        self._audience_file_path = file_path
        self.set_parameter('Create Matched Audience', 'Audience File Path', file_path)

    @property
    def suppression_file_path(self):
        return self._suppression_file_path

    @suppression_file_path.setter
    def suppression_file_path(self, sup_file_path):
        self._suppression_file_path = sup_file_path
        self.set_parameter('Suppression', 'Suppression File Path', sup_file_path)

    @property
    def audience_identifier(self):
        return self._audience_identifier

    @audience_identifier.setter
    def audience_identifier(self, audience_identifier):
        self._audience_identifier = audience_identifier
        self.set_parameter('Create Matched Audience', 'Audience Field Identifier', audience_identifier)
