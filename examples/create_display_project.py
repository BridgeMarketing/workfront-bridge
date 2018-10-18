from workfront.workfront import Workfront
from workfront_bridge.projects import display_builder

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()
b = display_builder.DisplayProjectBuilder(wf, "Test display project")
b.add_creative(
    creative_name='Test Creative 1',
    clickthrough_url='Test Clickthrough URL',
    landing_page_url='Test Landing Page URL',
    image_s3_url='Test Image S3 URL',
    creative_size='300x250',
)
b.add_creative(
    creative_name='Test Creative 2',
    clickthrough_url='Test Clickthrough URL 2',
    landing_page_url='Test Landing Page URL 2',
    image_s3_url='Test Image S3 URL 2',
    creative_size='300x250',
)
(b.
 set_start_date_inclusive_utc('2018-11-01').
 set_end_date_exclusive_utc('2018-12-01').
 set_campaign_name('Test Campaign').
 set_ad_group_name('Test AdGroup').
 set_adg_base_bid_amount(2.4))
prj = b.build()
prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})
print(prj)
