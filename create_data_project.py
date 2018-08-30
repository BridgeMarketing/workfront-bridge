from workfront.workfront import Workfront
from workfront_bridge.projects import match_and_export_builder

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()

b = match_and_export_builder.MatchAndExportProjectBuilder(wf, "Test match and export project builder 1")
prj = (b.set_audience_name('Sarlanga')
        .set_audience_file_path('s3://bridge-file-assets/API_files/orderID_1239/Channel_0'
                                '/5b575e51000bcb1d2cea4a5532889aee_26_20180828190332.csv')
        .build())

print(prj)
