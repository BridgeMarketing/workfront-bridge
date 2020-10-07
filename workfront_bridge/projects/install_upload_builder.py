from workfront_bridge.projects.install_upload import WFProjectInstallUpload
from workfront_bridge.projects.ttd import TTDBuilderMixin
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.blocks.base import WFBlockParser


class InstallUploadProjectBuilder(TTDBuilderMixin):
    """
    @summary: Audio project builder
    """

    def __init__(self, wf, project_name):
        """
        @param wf: Workfront service object
        @param project_name: project name in Workfront
        """
        self.project_name = project_name
        self.wf = wf

        # project level
        self._install_file_s3_url = None
        self._project_type = None

    def build_project(self):
        project = WFProjectInstallUpload(self.project_name)
        project.install_file_s3_url = self._install_file_s3_url
        project.project_type = self._project_type
        return project

    def build(self):
        """
        @summary: build the Workfront project.
        @raise WFBrigeException
        @return: WFProject object
        """

        project = self.build_project()
        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)
        return wf_project

    def set_project_type(self, v):
        self._project_type = v
        return self

    def set_install_file_s3_url(self, v):
        self._install_file_s3_url = v
        return self
