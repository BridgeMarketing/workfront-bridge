from workfront.workfront import Workfront
from workfront_bridge.projects import cancel_builder

# Project being cancelled
WF_EMAIL_PROJECT_ID = "5b8d644e00080396342da31be1926815"

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()

b = cancel_builder.CancelProjectBuilder(wf)
b.set_project_to_cancel(WF_EMAIL_PROJECT_ID)
prj = b.build()

print prj
