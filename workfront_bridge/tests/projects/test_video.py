import mock
import datetime

from workfront_bridge.tests.projects.base import BaseBuilderTest
from workfront_bridge.projects import video_builder


class Test_Video_Builder(BaseBuilderTest):
    def setUp(self):
        super(Test_Video_Builder, self).setUp()

        self.wf = mock.MagicMock()
        self.builder = video_builder.VideoProjectBuilder(self.wf, "Test - Video project")

    def test_video(self):
        self.builder.add_ad_group(
            ad_group_name='Test AdGroup 1',
            device_type='ConnectedTV',
            creatives=[
                {
                    'creative_name': 'Test Creative 1',
                    'media_s3_url': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/video.mp4',
                    'duration': 15,
                    'clickthrough_url': 'http://a.com/',
                    'landing_page_url': 'http://a.com/',
                    'third_party_impression_tracking_url': 'http://dummy.com',
                },
            ]
        )

        (self.builder.set_ttd_advertiser_id('xc7votu')
                     .set_audience_name('audience_name')
                     .set_start_date_inclusive_utc(datetime.datetime.strptime('2019-04-29', '%Y-%m-%d'))
                     .set_end_date_exclusive_utc(datetime.datetime.strptime('2019-05-02', '%Y-%m-%d'))
                     .set_campaign_name('Test Campaign')
                     .set_multiple_ad_groups(False)
                     .set_project_type('Video'))

        prj = self.builder.build()

        expected = {
            'wf_template_name': 'Base Project Container - Video Channel',
            '': {
                'MultipleAdGroups': 'False',
                'Project Type': 'Video',
                'TTDAdvertiserID': 'xc7votu'
            },
            'blocks': [
                {
                    'wf_template_name': 'Block - Display Data',
                    'Create Audience': {
                        'Audience Name': 'audience_name',
                        'type': 'DigitalAudienceCreate',
                    },
                },
                {
                    'wf_template_name': 'Block - Display Campaign v2',
                    'Create Campaign & Flight': {
                        'Campaign Name': 'Test Campaign',
                        'EndDateTimeExclusiveUTC': '2019-05-02T00:00:00.000+0000',
                        'StartDateTimeInclusiveUTC': '2019-04-29T00:00:00.000+0000',
                        'type': 'VideoCampaignCreate',
                    },
                },
                {
                    'wf_template_name': 'Block - Display Ad Group Setup',
                    'blocks': [
                        {
                            'wf_template_name': 'Block - Media Creative Upload',
                            'Creative Upload': {
                                'ClickthroughUrl': 'http://a.com/',
                                'Creative Name': 'Test Creative 1',
                                'LandingPageUrl': 'http://a.com/',
                                'ThirdPartyImpressionTrackingUrl': 'http://dummy.com',
                                'MediaS3URL': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/video.mp4',
                                'Duration': '15',
                                'type': 'VideoCreativeUpload',
                            }
                        },
                        {
                            'wf_template_name': 'Block - Display Create Ad Group',
                            'Create Ad Group': {
                                'AdGroupName': 'Test AdGroup 1',
                                'Device Type': 'ConnectedTV',
                                'type': 'VideoAdGroupCreate',
                            }
                        },
                    ]
                },
                {
                    'wf_template_name': 'Block - Display QA',
                    'blocks': [
                        {
                            'wf_template_name': 'Block - Media QA Creative',
                            'Creative QA': {
                                'ClickthroughUrl': 'http://a.com/',
                                'Creative Name': 'Test Creative 1',
                                'LandingPageUrl': 'http://a.com/',
                                'ThirdPartyImpressionTrackingUrl': 'http://dummy.com',
                                'MediaS3URL': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/video.mp4',
                                'Duration': '15',
                            }
                        },
                        {
                            'wf_template_name': 'Block - Display QA Ad Group v2',
                            'Ad Group QA': {
                                'AdGroupName': 'Test AdGroup 1',
                                'Campaign Name': 'Test Campaign',
                                'Device Type': 'ConnectedTV',
                                'EndDateTimeExclusiveUTC': '2019-05-02T00:00:00.000+0000',
                                'StartDateTimeInclusiveUTC': '2019-04-29T00:00:00.000+0000'
                            }
                        },
                    ]
                },
                {
                    'wf_template_name': 'Block - Display Launch',
                }
            ]
        }

        self.assertDeepEquals(expected, prj)
