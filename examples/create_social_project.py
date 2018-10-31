from workfront.workfront import Workfront
from workfront_bridge.projects import social_builder
from datetime import datetime


wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()
b = social_builder.SocialProjectBuilder(wf, "Test - Social project")
# TODO: campaign fields
(b
 .set_provider('Facebook')
 .set_campaign_title('Test Social Campaign Title'))
ad_group_1 = {
    'number_of_impressions': 1000,
    'impressions_or_clicks': 'Impressions',
    'datetime_start': datetime(2018, 11, 1, 10, 0, 0),
    'datetime_end': datetime(2018, 12, 1, 10, 0, 0),
    'device_type': ['Mobile', 'Desktop'],
    'bid_amount': 20,
    'mobile_os': ['Android', 'iOS'],
    'budget_daily_or_lifetime': 'Lifetime',
    'creatives': [
        {
            'creative_type': 'image',
            'title': 'Test Creative 1',
            's3_uri': 's3://example/uri/1',
            'description': 'Test Description 1',
            'message': 'Creative Message 1',
            'advertiser_website_url': 'http:google.com',
            'fb_call_to_action': 'Learn More',
        },
        {
            'creative_type': 'image',
            'title': 'Test Creative 2',
            's3_uri': 's3://example/uri/2',
            'description': 'Test Description 2',
            'message': 'Creative Message 2',
            'advertiser_website_url': 'http:google.com',
            'fb_call_to_action': 'Learn More',
        },
    ]
}
b.add_ad_group(ad_group_1)
prj = b.build()
prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})
print(prj)
