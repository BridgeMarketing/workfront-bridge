from workfront.workfront import Workfront
from datetime import datetime
from workfront_bridge.projects import email_test_list_builder

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')

wf.login()

b = email_test_list_builder.EmailTestListProjectBuilder(wf, "Test list test project")

b.add_test_list("s3://some/testlist1.csv")

b.set_ecm_html("s3://some/creative.html")

b.set_deployment_datetime(datetime(2020, 2, 3, 14, 29, 22))

b.set_subject("asuntoooo")

b.set_seeds_provider("Jango")
b.set_seeds_sender_email("seedssender@email.com")
b.set_seeds_sender_name("Seed Name")

b.set_email_creative_id("10")

prj = b.build()
prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})

print prj
