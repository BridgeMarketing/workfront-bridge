from workfront.workfront import Workfront
from workfront_bridge.projects import update_builder
from datetime import datetime

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060',
               'thebridgecorp.sb01.workfront.com')
wf.login()

b = update_builder.UpdateProjectBuilder(wf)
b.set_project_to_update('5b8ea4cb000aef1526c4001001ba24c7')
b.set_datetime_to_update(datetime.now())
perri = b.build()

print(perri)
