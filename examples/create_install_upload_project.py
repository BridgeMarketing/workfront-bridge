import datetime
from workfront.workfront import Workfront
from workfront_bridge.projects import install_upload_builder


wf = Workfront(
    "notifications@wf.bridgemarketing.com",
    "beef6060",
    "thebridgecorp.sb01.workfront.com",
)
wf.login()
b = install_upload_builder.InstallUploadProjectBuilder(
    wf, "Test - Install Upload project"
)
(
    b.set_install_file_s3_url(
        "s3://bridge-file-assets/Installs/Install_File.csv"
    ).set_project_type("Upload Install")
)

prj = b.build()
prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})
print(prj)
