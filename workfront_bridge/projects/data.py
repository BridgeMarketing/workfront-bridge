from workfront_bridge.blocks.base import WFBlock


class WFProjectDataContainer(WFBlock):
    """
    @summary: Workfront Data Project Container.
    Use this project container to create workfront M&E or B2C projects.
    This project container has no tasks in it but has all the fields of the
    custom forms that a M&E or B2C project needs.
    """

    template_name = "Base Project Container - Data"

    block_params = {
        '': [
            ('Project Type', 'project_type', True),
            ('Audience Id', 'audience_id', False),
            ('Audience File Path', 'audience_file_path', False),
            ('Data Task Id', 'data_task_id', False),
            ('Suppression Task Ids', 'suppression_task_ids', False, lambda v: ','.join(v)),
        ],
    }

    def __init__(self, prj_name):
        super(WFProjectDataContainer, self).__init__(self.template_name, name=prj_name)

    def set_b2c(self):
        self.project_type = "Data"

    def set_match_and_export(self):
        self.project_type = "Match Export"

    def set_10x_data(self):
        self.project_type = "Data 10x"
