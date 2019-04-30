import mock
import datetime

from workfront_bridge.tests.projects.base import BaseBuilderTest
from workfront_bridge.projects import audio_builder


class Test_Audio_Builder(BaseBuilderTest):
    def setUp(self):
        super(Test_Audio_Builder, self).setUp()

        self.wf = mock.MagicMock()
        self.builder = audio_builder.AudioProjectBuilder(self.wf, "Test - Audio project")

    def test_audio(self):
        self.builder.add_ad_group(
            ad_group_name='Test AdGroup 1',
            creatives=[
                {
                    'creative_name': 'Test Creative 1',
                    'audio_s3_url': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/sound.mp3',
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
                     .set_project_type('Audio'))

        prj = self.builder.build()

        expected = {
            'wf_template_name': 'Base Project Container - Audio Channel',
            '': {
                'MultipleAdGroups': 'False',
                'Project Type': 'Audio',
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
                        'type': 'AudioCampaignCreate',
                    },
                },
                {
                    'wf_template_name': 'Block - Display Ad Group Setup',
                    'blocks': [
                        {
                            'wf_template_name': 'Block - Audio Creative Upload',
                            'Creative Upload': {
                                'ClickthroughUrl': 'http://a.com/',
                                'Creative Name': 'Test Creative 1',
                                'LandingPageUrl': 'http://a.com/',
                                'ThirdPartyImpressionTrackingUrl': 'http://dummy.com',
                                'AudioS3URL': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/sound.mp3',
                                'Duration': '15',
                                'type': 'AudioCreativeUpload',
                            }
                        },
                        {
                            'wf_template_name': 'Block - Display Create Ad Group',
                            'Create Ad Group': {
                                'AdGroupName': 'Test AdGroup 1',
                                'type': 'AudioAdGroupCreate',
                            }
                        },
                    ]
                },
                {
                    'wf_template_name': 'Block - Display QA',
                    'blocks': [
                        {
                            'wf_template_name': 'Block - Audio QA Creative',
                            'Creative QA': {
                                'ClickthroughUrl': 'http://a.com/',
                                'Creative Name': 'Test Creative 1',
                                'LandingPageUrl': 'http://a.com/',
                                'ThirdPartyImpressionTrackingUrl': 'http://dummy.com',
                                'AudioS3URL': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/sound.mp3',
                                'Duration': '15',
                            }
                        },
                        {
                            'wf_template_name': 'Block - Display QA Ad Group v2',
                            'Ad Group QA': {
                                'AdGroupName': 'Test AdGroup 1',
                                'Campaign Name': 'Test Campaign',
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
