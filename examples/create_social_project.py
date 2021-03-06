from workfront.workfront import Workfront
from workfront_bridge.projects import social_builder
from datetime import datetime

S3_PATH = 's3://pbm-ccm-stg-ccmbucket/V2_SOCIAL_TEST/'
wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()
b = social_builder.SocialProjectBuilder(wf, "Test - Social project")
(b
 .set_provider('Facebook')
 .set_campaign_title('Test Social Campaign Title')
 .set_fb_page_id('1355309931178027'))
ad_group_1 = {
    'fb_placement': 'FB Feeds',
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
            's3_uri': S3_PATH + 'dog.jpeg',
            'description': 'Test Description 1',
            'message': 'Creative Message 1',
            'advertiser_website_url': 'http:google.com',
            'fb_call_to_action': 'Learn More',
        },
        {
            'creative_type': 'image',
            'title': 'Test Creative 2',
            's3_uri': S3_PATH + 'cat.jpeg',
            'description': 'Test Description 2',
            'message': 'Creative Message 2',
            'advertiser_website_url': 'http:google.com',
            'fb_call_to_action': 'Learn More',
        },
    ]
}
b.add_ad_group(ad_group_1)
ad_group_2 = {
    'fb_placement': 'FB Right Column',
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
            'title': 'Test Creative 3',
            's3_uri': S3_PATH + 'angry_lion.jpg',
            'description': 'Test Description 3',
            'message': 'Creative Message 3',
            'advertiser_website_url': 'http:google.com',
            'fb_call_to_action': 'Learn More',
        },
        {
            'creative_type': 'image',
            'title': 'Test Creative 4',
            's3_uri': S3_PATH + 'zebra.jpg',
            'description': 'Test Description 4',
            'message': 'Creative Message 4',
            'advertiser_website_url': 'http:google.com',
            'fb_call_to_action': 'Learn More',
        },
    ]
}
b.add_ad_group(ad_group_2)
ad_group_3 = {
    'fb_placement': 'IG Feed',
    'number_of_impressions': 1500,
    'impressions_or_clicks': 'Impressions',
    'datetime_start': datetime(2018, 11, 1, 10, 0, 0),
    'datetime_end': datetime(2018, 12, 1, 10, 0, 0),
    'device_type': ['Mobile', 'Desktop'],
    'bid_amount': 10,
    'mobile_os': ['Android', 'iOS'],
    'budget_daily_or_lifetime': 'Lifetime',
    'creatives': [
        {
            'creative_type': 'image',
            'title': 'Test Creative 5',
            's3_uri': S3_PATH + 'bunny.jpg',
            'description': 'Test Description 5',
            'message': 'Creative Message 5',
            'advertiser_website_url': 'http:google.com',
            'fb_call_to_action': 'Learn More',
        },
        {
            'creative_type': 'image',
            'title': 'Test Creative 6',
            's3_uri': S3_PATH + 'goat.jpg',
            'description': 'Test Description 6',
            'message': 'Creative Message 6',
            'advertiser_website_url': 'http:google.com',
            'fb_call_to_action': 'Learn More',
        },
    ]
}
b.add_ad_group(ad_group_3)

prj = b.build()
prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})
print(prj)
