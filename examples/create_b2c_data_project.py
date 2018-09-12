from workfront.workfront import Workfront
from workfront_bridge.projects import b2c_builder

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060',
               'thebridgecorp.sb01.workfront.com')
wf.login()

b = b2c_builder.B2CProjectBuilder(wf, "Test B2C project builder")
prj = b.set_count_id("COUNTID_1234").build()

print(prj)
