from workfront_bridge.projects.installs.install_deactivate import WFProjectInstallDeactivate
from workfront_bridge.projects.installs.install_upload_builder import InstallUploadProjectBuilder

class InstallDeactivateProjectBuilder(InstallUploadProjectBuilder):
    """
    @summary: Deactivate Install project builder
    """

    def build_project(self):
        project = WFProjectInstallDeactivate(self.project_name)
        project.install_file_s3_url = self._install_file_s3_url
        project.project_type = self._project_type
        project.account_id = self._account_id
        project.install_id = self._install_id
        project.installation_date = self._installation_date
        return project
