from workfront.workfront import Workfront
from workfront_bridge.projects import data_builder


def simple_b2c(wf):
    b = data_builder.DataProjectBuilder(wf, "Test B2C project builder")
    prj = b.set_b2c()\
           .set_count_id(["COUNTID_12", "COUNTID_34", "COUNTID_56"]) \
           .build()
    return prj


def b2c_with_suppression_type(wf):
    b = data_builder.DataProjectBuilder(wf, "Test B2C project builder")
    prj = b.set_b2c()\
           .set_count_id("COUNTID_1234")\
           .set_suppression_type("one_per_person")\
           .build()
    return prj


def b2c_with_suppression_files(wf):
    b = data_builder.DataProjectBuilder(wf, "Test B2C project builder")
    prj = b.set_b2c()\
           .set_count_id("COUNTID_1234")\
           .add_suppression_file("s3://some/ids.txt", "bridge_id")\
           .add_suppression_file("s3://some/emails.txt", "email")\
           .build()
    return prj


def b2c_with_suppressions(wf):
    b = data_builder.DataProjectBuilder(wf, "Test B2C project builder")
    prj = b.set_b2c()\
           .set_count_id("COUNTID_1234")\
           .set_suppression_type("one_per_person")\
           .add_suppression_file("s3://some/emails.txt", "email")\
           .build()
    return prj


wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060',
               'thebridgecorp.sb01.workfront.com')

print(simple_b2c(wf))

print(b2c_with_suppression_type(wf))

print(b2c_with_suppression_files(wf))

print(b2c_with_suppressions(wf))
