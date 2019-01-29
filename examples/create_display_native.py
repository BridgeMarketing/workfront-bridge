from workfront.workfront import Workfront
from workfront_bridge.projects import display_builder
import datetime

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()
b = display_builder.DisplayProjectBuilder(wf, "Test display project")
b.add_ad_group(
    ad_group_name='Test AdGroup 1',
    creatives=[
        {
            'creative_type': 'Image Native',
            'creative_name': 'Test Creative 6',
            'clickthrough_url': 'http://dummy.com',
            'landing_page_url': 'http://dummy.com',
            'third_party_impression_tracking_url': 'http://dummy.com',
            'native_text_asset_title_long': 'native_text_asset_title_long',
            'native_text_asset_title_short': 'native_text_asset_title_short',
            'native_text_asset_sponsor': 'native_text_asset_sponsor',
            'native_text_asset_description_long': 'native_text_asset_description_long',
            'native_text_asset_description_short': 'native_text_asset_description_short',
        }
    ]
)
(b.set_ttd_advertiser_id('xc7votu')
 .set_audience_name('audience_name')
 .set_start_date_inclusive_utc(datetime.datetime.utcnow())
 .set_end_date_exclusive_utc(datetime.datetime.utcnow() + datetime.timedelta(days=3))
 .set_campaign_name('Test Campaign')
 .set_multiple_ad_groups(True)
 .set_project_type('Display - Desktop & Mobile'))
prj = b.build()
prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})
print(prj)
