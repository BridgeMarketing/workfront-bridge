from datetime import datetime

from workfront.workfront import Workfront


# Project being paused
from workfront_bridge.projects.resume_builder import ResumeProjectBuilder

WF_EMAIL_PROJECT_ID = "5b8d644e00080396342da31be1926815"

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()

b = ResumeProjectBuilder(wf)
b.set_project_to_resume(WF_EMAIL_PROJECT_ID)
b.set_datetime_to_update(datetime.now())

prj = b.build()

print prj
