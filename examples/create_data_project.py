from workfront.workfront import Workfront
from workfront_bridge.projects import data_builder


def simple_single_segment(wf):
    b = data_builder.DataProjectBuilder(wf, "Test segment project builder")
    b.add_audience_segment(count_id="COUNTID_1234",
                           segment_type="B2C",
                           audience_file_path=None,
                           audience_name=None,
                           audience_identifier=None)
    prj = b.build()
    return prj


def simple_segment_with_suppression_type(wf):
    b = data_builder.DataProjectBuilder(wf, "Test segment project builder")
    b.add_audience_segment(count_id="COUNTID_1234",
                           segment_type="B2C",
                           audience_file_path=None,
                           audience_name=None,
                           audience_identifier=None)
    b.add_audience_segment(count_id=None,
                           segment_type="ME",
                           audience_file_path="s3://test_bucket/test_path/test_file.csv",
                           audience_name="test_audience",
                           audience_identifier="bridge_id")
    b.set_suppression_type("one_per_person")
    prj = b.build()
    return prj


def simple_segment_with_suppression_files(wf):
    b = data_builder.DataProjectBuilder(wf, "Test segment project builder")
    b.add_audience_segment(count_id=None,
                           segment_type="ME",
                           audience_file_path="s3://test_bucket/test_path/test_file.csv",
                           audience_name="test_audience",
                           audience_identifier="bridge_id")
    b.add_audience_segment(count_id="COUNTID_1234",
                           segment_type="B2C",
                           audience_file_path=None,
                           audience_name=None,
                           audience_identifier=None)
    b.add_audience_segment(count_id=None,
                           segment_type="ME",
                           audience_file_path="s3://test_bucket/test_path/test_file.csv",
                           audience_name="test_audience",
                           audience_identifier="bridge_id")
    b.add_suppression_file("s3://some/ids.txt", "bridge_id")
    b.add_suppression_file("s3://some/emails.txt", "email")
    prj = b.build()
    return prj


wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060',
               'thebridgecorp.sb01.workfront.com')

print(simple_single_segment(wf))

print(simple_segment_with_suppression_type(wf))

print(simple_segment_with_suppression_files(wf))
