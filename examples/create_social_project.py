from workfront.workfront import Workfront
from workfront_bridge.projects import social_builder
from datetime import datetime


wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()
b = social_builder.SocialProjectBuilder(wf, "Test - Social project")
(b.set_number_of_impressions(1000)
 .set_impressions_or_clicks('Impressions')
 .set_datetime_start(datetime(2018, 11, 1, 10, 0, 0))
 .set_datetime_end(datetime(2018, 12, 1, 10, 0, 0))
 .set_campaign_title('Test Campaign Title')
 .set_device_type(['Mobile', 'Desktop'])
 .set_bid_amount(20)
 .set_mobile_os(['Android', 'iOS'])
 .set_budget_daily_or_lifetime('Lifetime')
 .set_provider('FB+IG')
 )
b.add_creative(
    creative_type='image',
    title='Test Creative 1',
    s3_uri='s3://example/uri/1',
    description='Test Description 1',
    message='Creative Message 1',
    advertiser_website_url='http:google.com',
    fb_call_to_action='Learn More',
    fb_facebook_platforms=['Feeds', 'Right Column'],
    fb_instagram_platforms=['Feed'],
)
b.add_creative(
    creative_type='video',
    title='Test Creative 2',
    s3_uri='s3://example/uri/2',
    image_s3_uri='s3://example/uri/3',
    message='Creative Message 2',
    advertiser_website_url='http:google.com',
    fb_call_to_action='Learn More',
    fb_facebook_platforms=['Feeds', 'Right Column'],
    fb_instagram_platforms=['Feed'],
)
prj = b.build()
prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})
print(prj)
