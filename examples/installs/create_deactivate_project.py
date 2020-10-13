from datetime import datetime
from workfront.workfront import Workfront
from workfront_bridge.projects.installs.install_deactivate_builder import InstallDeactivateProjectBuilder


wf = Workfront(
    "notifications@wf.bridgemarketing.com",
    "beef6060",
    "thebridgecorp.sb01.workfront.com",
)
wf.login()
b = InstallDeactivateProjectBuilder(
    wf, "Test - Install Deactivate project"
)

b.set_install_file_s3_url("s3://bridge-file-assets/Installs/Install_File.csv")\
    .set_project_type("Upload Install")\
    .set_install_id(45)\
    .set_account_id(105)\
    .set_installation_date(datetime.now())

prj = b.build()
prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})
print(prj)
