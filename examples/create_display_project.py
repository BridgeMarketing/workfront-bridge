from workfront.workfront import Workfront
from workfront_bridge.projects import display_builder

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()
b = display_builder.DisplayProjectBuilder(wf, "Test display project builder 1")
prj = b.build()
print(prj)
