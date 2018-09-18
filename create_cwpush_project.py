from workfront.workfront import Workfront
from workfront_bridge.projects import cwpush_builder
from datetime import datetime

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()

b = cwpush_builder.CWToolProjectBuilder(wf, "Test cwpush project builder 1")
b.bridge_order_id = '12345'
b.start_date = datetime.now()
prj = b.build()
print(prj)
