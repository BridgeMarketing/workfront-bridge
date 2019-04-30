from workfront.workfront import Workfront
from workfront_bridge.projects import data_builder


def simple_mye(wf):
    b = data_builder.DataProjectBuilder(wf, "Test M&E project builder 1")
    prj = b.set_match_and_export()\
           .set_audience_name('Sarlanga')\
           .set_audience_file_path('s3://some/emails.txt')\
           .set_audience_identifier("email")\
           .build()
    return prj


def mye_with_suppressions(wf):
    b = data_builder.DataProjectBuilder(wf, "Test M&E project builder 2")
    prj = b.set_match_and_export()\
           .set_audience_name('Sarlanga')\
           .set_audience_file_path('s3://some/ids.txt')\
           .set_audience_identifier("bridge_id")\
           .set_suppression_type("one_per_person")\
           .add_suppression_file("s3://some/emails.txt", "email")\
           .build()
    return prj


wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060',
               'thebridgecorp.sb01.workfront.com')

print(simple_mye(wf))

print(mye_with_suppressions(wf))
