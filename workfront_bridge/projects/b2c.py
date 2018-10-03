from workfront_bridge.blocks.base import WFBlock


class WFProjectB2CContainer(WFBlock):
    """
    @summary: Workfront Data B2C Project Container.
    """

    template_name = "Base Project Container - Data B2C (DEV)"

    def __init__(self, prj_name):
        super(WFProjectB2CContainer, self).__init__(self.template_name,
                                                    name=prj_name)

        opt = [
            "Audience Id",
            "Audience File Path",
            "Data Task Id",
            "Suppression Task Ids"
        ]
        self._add_optional_parameters(opt)

        # Project Container fields:
        self._audience_id = None
        self._audience_file_path = None
        self._data_task_id = None
        self._suppression_task_ids = None

    @property
    def audience_id(self):
        return self._audience_id

    @audience_id.setter
    def audience_id(self, v):
        self._audience_id = v
        self.set_parameter("", "Audience Id", v)

    @property
    def audience_file_path(self):
        return self._audience_file_path

    @audience_file_path.setter
    def audience_file_path(self, v):
        self._audience_file_path = v
        self.set_parameter("", "Audience File Path", v)

    @property
    def data_task_id(self):
        return self._data_task_id

    @data_task_id.setter
    def data_task_id(self, v):
        self._data_task_id = v
        self.set_parameter("", "Data Task Id", v)

    @property
    def suppression_task_ids(self):
        return self._suppression_task_ids

    @suppression_task_ids.setter
    def suppression_task_ids(self, v):
        self._suppression_task_ids = v
        self.set_parameter("", "Suppression Task Ids", v)