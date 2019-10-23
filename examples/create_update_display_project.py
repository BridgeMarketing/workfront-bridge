from workfront.workfront import Workfront
from workfront_bridge.projects import update_builder
import datetime

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060',
               'thebridgecorp.sb01.workfront.com')
wf.login()

b = update_builder.UpdateProjectBuilder(wf)
b.set_project_to_update('5d8e2bfe00050612ce6351799e0ee557')
b.set_new_start_datetime(datetime.datetime.now())
b.set_new_end_datetime(datetime.datetime.now() + datetime.timedelta(days=10))
new_project = b.build()

print(new_project)
