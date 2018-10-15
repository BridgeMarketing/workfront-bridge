from workfront.workfront import Workfront
from workfront_bridge.projects import cwpush_builder

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()
b = cwpush_builder.CWPushProjectBuilder(wf, "Test cwpush project builder 1")
b.bridge_order_id = '12345'
b.partner_name = 'Partner Name'
b.industry = 'Arts & Entertainment'
b.target_volume = 500
b.click_tier = 'CL'
b.open_tier = 'O1'
prj = b.build()
print(prj)
