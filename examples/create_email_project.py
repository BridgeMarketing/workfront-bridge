from workfront.workfront import Workfront
from datetime import datetime
from workfront_bridge.projects import email_builder

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')

wf.login()

b = email_builder.EmailProjectBuilder(wf, "Test pablo email project builder 1")

b.set_html("s3://some/creative.html")

b.set_deployment_datetime(datetime(2020, 2, 3, 14, 29, 22))
b.set_seed_list("s3://some/seed.csv")

b.set_subject("asuntoooo")
b.set_subject_test_prefix("prefijooooo")
b.set_send_validate_test_seed_emails(True)

b.set_audience_provider("ActOn")
b.set_audience_sender_email("audience_sender@email.com")
b.set_audience_sender_name("Sender NAME")

b.set_live_seeds_provider("Jango")
b.set_live_seeds_sender_email("liveseedssender@email.com")
b.set_live_seeds_sender_name("Live Seed Name")

b.set_email_creative_id("10")
b.set_lr_account_id('abcedfg1')
b.set_lr_bonus_media_account_id('abcedfg1')

prj = b.build()
prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})

print prj
