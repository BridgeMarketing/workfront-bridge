from workfront.workfront import Workfront
from workfront_bridge.projects import data_builder


def simple_retargeting_project(wf):
    b = data_builder.DataProjectBuilder(wf, "Test Retargeting Data project builder")
    b.set_retargeting_data(retargeting_type="Openers", provider_name="ongage", provider_campaign_id="hj12f3")
    prj = b.build()
    return prj


wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060',
               'thebridgecorp.sb01.workfront.com')

print(simple_retargeting_project(wf))
