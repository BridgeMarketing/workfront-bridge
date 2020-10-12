from workfront_bridge.blocks.base import WFBlock


class WFProjectInstallDeactivate(WFBlock):
    """
    @summary: Workfront Deactivate Install Project.
    Use this project to create Workfront Deactivate Install tasks.
    The container has tasks,and level fields.
    """

    template_name = "Install - Deactivate"

    block_params = {
        "": [
            ("Project Type", "project_type", False),
            ("install_file_s3_url", "install_file_s3_url", False),
            ("account_id", "account_id", False),
            ("install_id", "install_id", False),
            ("installation_date", "installation_date", False),
        ],
    }

    def __init__(self, prj_name):
        super(WFProjectInstallDeactivate, self).__init__(self.template_name, name=prj_name)
