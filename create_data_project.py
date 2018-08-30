from workfront.workfront import Workfront
from workfront_bridge.projects import match_and_export_builder

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()

b = match_and_export_builder.MatchAndExportProjectBuilder(wf, "Test match and export project builder 1")
b.audience_name = 'audience_name_1'
b.audience_file_path = 'audience_file_path_1'
b.suppression_file_path = 's3://example/lala.csv'
b.audience_id = 'audience_id_1'
b.data_task_id = 1
b.suppression_task_ids = ['1', '2', '3']

prj = b.build()
print(prj)
