import datetime
from workfront.workfront import Workfront
from workfront_bridge.projects import video_builder


wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()
b = video_builder.VideoProjectBuilder(wf, "Test - Video project")
b.add_ad_group(
    ad_group_name='Test AdGroup 1',
    device_type='ConnectedTV',
    creatives=[
        {
            'creative_name': 'Test Creative 1',
            'media_s3_url': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/video.mp4',
            'duration': 30,
            'clickthrough_url': 'http://a.com/',
            'landing_page_url': 'http://a.com/',
            'third_party_impression_tracking_url': 'http://dummy.com'
        },
    ]
)
(b.set_ttd_advertiser_id('xc7votu')
 .set_audience_name('audience_name')
 .set_start_date_inclusive_utc(datetime.datetime.utcnow())
 .set_end_date_exclusive_utc(datetime.datetime.utcnow() + datetime.timedelta(days=3))
 .set_campaign_name('Test Campaign')
 .set_multiple_ad_groups(True)
 .set_project_type('Video'))
prj = b.build()
prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})
print(prj)
