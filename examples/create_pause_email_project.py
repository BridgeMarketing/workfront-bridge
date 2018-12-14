from workfront.workfront import Workfront


from workfront_bridge.projects.pause_builder import PauseProjectBuilder

# Project being paused
WF_EMAIL_PROJECT_ID = "5b8d644e00080396342da31be1926815"

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()

b = PauseProjectBuilder(wf)
b.set_project_to_pause(WF_EMAIL_PROJECT_ID)
prj = b.build()

print prj
