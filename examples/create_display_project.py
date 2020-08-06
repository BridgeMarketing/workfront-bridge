from workfront.workfront import Workfront
from workfront_bridge.projects import display_builder
import datetime

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()
b = display_builder.DisplayProjectBuilder(wf, "Test display project")
b.add_ad_group(
    ad_group_name='Test AdGroup 1',
    device_type=['PC'],
    creatives=[
        {
            'creative_type': 'Image Banner or Interstitial',
            'creative_name': 'Test Creative 1',
            'clickthrough_url': 'http://dummy.com',
            'landing_page_url': 'http://dummy.com',
            'image_s3_url': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/mobile_banner.png',
            'creative_size': '300x250',
            'third_party_impression_tracking_url': 'http://dummy.com'
        },
        {
            'creative_type': 'Image Banner or Interstitial',
            'creative_name': 'Test Creative 2',
            'clickthrough_url': 'http://dummy.com',
            'landing_page_url': 'http://dummy.com',
            'image_s3_url': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/mobile_banner.png',
            'creative_size': '300x250',
            'third_party_impression_tracking_url': 'http://dummy.com'
        },
        {
            'creative_type': 'Image Banner or Interstitial',
            'creative_name': 'Test Creative 3',
            'clickthrough_url': 'http://dummy.com',
            'landing_page_url': 'http://dummy.com',
            'image_s3_url': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/mobile_banner.png',
            'creative_size': '300x250',
            'third_party_impression_tracking_url': 'http://dummy.com'
        },
    ]
)
b.add_ad_group(
    ad_group_name='Test AdGroup 2',
    adg_kpi_goal='seeAds',
    creatives=[
        {
            'creative_type': 'Image Banner or Interstitial',
            'creative_name': 'Test Creative 4',
            'clickthrough_url': 'http://dummy.com',
            'landing_page_url': 'http://dummy.com',
            'image_s3_url': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/mobile_banner.png',
            'creative_size': '300x250',
            'third_party_impression_tracking_url': 'http://dummy.com'
        },
        {
            'creative_type': 'Image Banner or Interstitial',
            'creative_name': 'Test Creative 5',
            'clickthrough_url': 'http://dummy.com',
            'landing_page_url': 'http://dummy.com',
            'image_s3_url': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/mobile_banner.png',
            'creative_size': '300x250',
            'third_party_impression_tracking_url': 'http://dummy.com'
        },
        {
            'creative_type': 'Image Banner or Interstitial',
            'creative_name': 'Test Creative 6',
            'clickthrough_url': 'http://dummy.com',
            'landing_page_url': 'http://dummy.com',
            'image_s3_url': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/mobile_banner.png',
            'creative_size': '300x250',
            'third_party_impression_tracking_url': 'http://dummy.com',
        },
    ]
)
(b.set_ttd_advertiser_id('xc7votu')
 .set_ttd_bonus_media_advertiser_id('xc7votu')
 .set_lr_account_id('abcdef1')
 .set_lr_bonus_media_account_id('abcdef1')
 .set_audience_name('audience_name')
 .set_start_date_inclusive_utc(datetime.datetime.utcnow())
 .set_end_date_exclusive_utc(datetime.datetime.utcnow() + datetime.timedelta(days=3))
 .set_campaign_name('Test Campaign')
 .set_multiple_ad_groups(True)
 .set_project_type('Display - Desktop & Mobile'))
prj = b.build()
prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})
print(prj)
