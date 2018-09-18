from workfront.workfront import Workfront
from workfront_bridge.projects.email_builder import EmailOnBoardingProjectBuilder

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060',
               'thebridgecorp.sb01.workfront.com')
wf.login()

b = EmailOnBoardingProjectBuilder(wf, "Test pelu stg blocks 20")

b.set_category("Automotive")
b.set_subject("Some_example_subject")
b.set_from_line("from line")
b.set_email_creative_id("1")

#b.set_html("s3://mtnmnz-prod-email-deployment-nty5nz/onboarding/client_5b4caf8e038474320f450332e75c4400/20180816184445_creative_unsub.html")
b.set_html("s3://bridge-file-assets/order/999/channels/a471ecc1-8b49-4ce5-838f-5bcf2cd60d46/html_file/Test_zip_(1).zip")

b.set_client_id("5b4caf8e038474320f450332e75c4400")
#b.set_client_id("5b45ff9b000aa3a5db15b2e269976a4c")

b.set_live_seed_list("s3://mtnmnz-prod-email-deployment-nty5nz/onboarding/client_5b4caf8e038474320f450332e75c4400/20180816184713_live_seeds.csv")

b.add_test_list("s3://mtnmnz-prod-email-deployment-nty5nz/onboarding/client_5b4caf8e038474320f450332e75c4400/20180816184718_test_seeds (6th copy).csv")
b.add_test_list("s3://mtnmnz-prod-email-deployment-nty5nz/onboarding/client_5b4caf8e038474320f450332e75c4400/20180816184721_test_seeds (5th copy).csv")
b.add_test_list("s3://mtnmnz-prod-email-deployment-nty5nz/onboarding/client_5b4caf8e038474320f450332e75c4400/20180816184721_test_seeds (5th copy).csv")
b.add_test_list("s3://mtnmnz-prod-email-deployment-nty5nz/onboarding/client_5b4caf8e038474320f450332e75c4400/20180816184721_test_seeds (5th copy).csv")
b.add_test_list("s3://mtnmnz-prod-email-deployment-nty5nz/onboarding/client_5b4caf8e038474320f450332e75c4400/20180816184721_test_seeds (5th copy).csv")

b.set_suppression_file_path("s3://mtnmnz-prod-email-deployment-nty5nz/onboarding/client_5b4caf8e038474320f450332e75c4400/20180816184708_suppression_file.csv")

p = b.build()

print p

