import datetime
from workfront.workfront import Workfront
from workfront_bridge.projects import audio_builder


wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()
b = audio_builder.AudioProjectBuilder(wf, "Test - Audio project")
b.add_ad_group(
    ad_group_name='Test AdGroup 1',
    creatives=[
        {
            'creative_name': 'Test Creative 1',
            'audio_s3_url': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/sound.mp3',
            'duration': 15,
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
 .set_project_type('Audio'))
prj = b.build()
prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})
print(prj)
