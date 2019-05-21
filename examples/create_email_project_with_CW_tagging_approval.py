from workfront.workfront import Workfront
from datetime import datetime
from workfront_bridge.projects import email_builder

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')

wf.login()


b = email_builder.EmailProjectBuilder(wf, "Test email project builder with CW Tagging")

b.add_tags_weight_approval_step = True

b.set_html("s3://some/creative.html")

b.set_deployment_datetime(datetime.now())
b.set_seed_list("s3://some/seed.csv")

b.set_subject("asuntoooo")
b.set_send_validate_test_seed_emails(True)

b.set_audience_provider("ActOn")
b.set_audience_sender_email("audience_sender@email.com")
b.set_audience_sender_name("Sender NAME")

b.set_live_seeds_provider("Jango")
b.set_live_seeds_sender_email("liveseedssender@email.com")
b.set_live_seeds_sender_name("Live Seed Name")

b.set_email_creative_id("10")

prj = b.build()

print prj
