import mock
import datetime

from workfront_bridge.tests.projects.base import BaseBuilderTest
from workfront_bridge.projects.installs import install_upload_builder


class Test_Install_Upload_Builder(BaseBuilderTest):
    def setUp(self):
        super(Test_Install_Upload_Builder, self).setUp()

        self.wf = mock.MagicMock()
        self.builder = install_upload_builder.InstallUploadProjectBuilder(
            self.wf, "Test - Install Upload project"
        )

    def test_install_upload(self):

        self.builder.set_project_type("Upload Install")
        self.builder.set_install_file_s3_url(
            "s3://bridge-file-assets/Installs/Install_File.csv"
        )
        self.builder.set_account_id('5')
        self.builder.set_install_id('555')
        self.builder.set_installation_date('2025-05-25')

        prj = self.builder.build()

        expected = {
            "wf_template_name": "Install - Upload",
            "": {
                "Project Type": "Upload Install",
                "install_file_s3_url": "s3://bridge-file-assets/Installs/Install_File.csv",
                "account_id": "5",
                "install_id": "555",
                "installation_date": "2025-05-25",
            },
        }

        self.assertEqual(expected, prj)
