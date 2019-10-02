from workfront.workfront import Workfront
from datetime import datetime
from workfront_bridge.projects import email_builder

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')

wf.login()


b = email_builder.EmailProjectBuilder(wf, "Test peluca email project builder without html validation")


b.set_is_created_from_onboarding(True)
b.set_ecm_html("s3://mtnmnz-prod-email-deployment-nty5nz/htmls/2018-09-18/5ba10c6c0043070842b08ca42a84e3d7/1432636334J5UC72.creative.html")

b.set_seed_list("s3://some/seed.csv")

b.set_subject("asuntoooo")

b.set_audience_provider("ActOn")
b.set_audience_sender_email("audience_sender@email.com")
b.set_audience_sender_name("Sender NAME")

b.set_deployment_datetime(datetime.now())

b.set_email_creative_id("100")

prj = b.build()

prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})

print prj
