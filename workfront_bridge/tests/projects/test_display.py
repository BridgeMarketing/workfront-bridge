import mock
import datetime

from workfront_bridge.tests.projects.base import BaseBuilderTest
from workfront_bridge.projects import display_builder


class Test_Display_Builder(BaseBuilderTest):
    def setUp(self):
        super(Test_Display_Builder, self).setUp()

        self.wf = mock.MagicMock()
        self.builder = display_builder.DisplayProjectBuilder(self.wf, "Test display project")

    def test_display_native(self):
        self.builder.add_ad_group(
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

        (self.builder.set_ttd_advertiser_id('xc7votu')
                     .set_audience_name('audience_name')
                     .set_start_date_inclusive_utc(datetime.datetime.strptime('2019-04-29', '%Y-%m-%d'))
                     .set_end_date_exclusive_utc(datetime.datetime.strptime('2019-05-02', '%Y-%m-%d'))
                     .set_campaign_name('Test Campaign')
                     .set_multiple_ad_groups(True)
                     .set_project_type('Display - Desktop & Mobile'))

        prj = self.builder.build()

        expected = {
            'wf_template_name': 'Base Project Container - Display Channel v2',
            '': {
                'MultipleAdGroups': 'True',
                'Project Type': 'Display - Desktop & Mobile',
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
                        'type': 'DigitalCampaignCreate',
                    },
                },
                {
                    'wf_template_name': 'Block - Display Ad Group Setup',
                    'blocks': [
                        {
                            'wf_template_name': 'Block - Display Creative Upload v2',
                            'Creative Upload': {
                                'ClickthroughUrl': 'http://dummy.com',
                                'Creative Name': 'Test Creative 6',
                                'DisplayCreativeType': 'Image Native',
                                'LandingPageUrl': 'http://dummy.com',
                                'NativeTextAssetDescriptionLong': 'native_text_asset_description_long',
                                'NativeTextAssetDescriptionShort': 'native_text_asset_description_short',
                                'NativeTextAssetSponsor': 'native_text_asset_sponsor',
                                'NativeTextAssetTitleLong': 'native_text_asset_title_long',
                                'NativeTextAssetTitleShort': 'native_text_asset_title_short',
                                'ThirdPartyImpressionTrackingUrl': 'http://dummy.com'
                            }
                        },
                        {
                            'wf_template_name': 'Block - Display Create Ad Group',
                            'Create Ad Group': {
                                'AdGroupName': 'Test AdGroup 1',
                                'type': 'DigitalDisplayAdGroupCreate',
                            }
                        },
                    ]
                },
                {
                    'wf_template_name': 'Block - Display QA',
                    'blocks': [
                        {
                            'wf_template_name': 'Block - Display QA Creative v2',
                            'Creative QA': {
                                'ClickthroughUrl': 'http://dummy.com',
                                'Creative Name': 'Test Creative 6',
                                'LandingPageUrl': 'http://dummy.com',
                                'NativeTextAssetDescriptionLong': 'native_text_asset_description_long',
                                'NativeTextAssetDescriptionShort': 'native_text_asset_description_short',
                                'NativeTextAssetSponsor': 'native_text_asset_sponsor',
                                'NativeTextAssetTitleLong': 'native_text_asset_title_long',
                                'NativeTextAssetTitleShort': 'native_text_asset_title_short',
                                'ThirdPartyImpressionTrackingUrl': 'http://dummy.com'
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

    def test_display_multi(self):
        self.builder.add_ad_group(
            ad_group_name='Test AdGroup 1',
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
            ]
        )
        self.builder.add_ad_group(
            ad_group_name='Test AdGroup 2',
            creatives=[
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

        (self.builder.set_ttd_advertiser_id('xc7votu')
                     .set_audience_name('audience_name')
                     .set_start_date_inclusive_utc(datetime.datetime.strptime('2019-04-29', '%Y-%m-%d'))
                     .set_end_date_exclusive_utc(datetime.datetime.strptime('2019-05-02', '%Y-%m-%d'))
                     .set_campaign_name('Test Campaign')
                     .set_multiple_ad_groups(True)
                     .set_project_type('Display - Desktop & Mobile'))

        prj = self.builder.build()

        expected = {
            'wf_template_name': 'Base Project Container - Display Channel v2',
            '': {
                'MultipleAdGroups': 'True',
                'Project Type': 'Display - Desktop & Mobile',
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
                        'type': 'DigitalCampaignCreate',
                    },
                },
                {
                    'wf_template_name': 'Block - Display Ad Group Setup',
                    'blocks': [
                        {
                            'wf_template_name': 'Block - Display Creative Upload v2',
                            'Creative Upload': {
                                'ClickthroughUrl': 'http://dummy.com',
                                'Creative Name': 'Test Creative 1',
                                'DisplayCreativeType': 'Image Banner or Interstitial',
                                'LandingPageUrl': 'http://dummy.com',
                                'ThirdPartyImpressionTrackingUrl': 'http://dummy.com',
                                'ImageS3URL': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/mobile_banner.png',
                            }
                        },
                        {
                            'wf_template_name': 'Block - Display Creative Upload v2',
                            'Creative Upload': {
                                'ClickthroughUrl': 'http://dummy.com',
                                'Creative Name': 'Test Creative 2',
                                'DisplayCreativeType': 'Image Banner or Interstitial',
                                'LandingPageUrl': 'http://dummy.com',
                                'ThirdPartyImpressionTrackingUrl': 'http://dummy.com',
                                'ImageS3URL': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/mobile_banner.png',
                            }
                        },
                        {
                            'wf_template_name': 'Block - Display Create Ad Group',
                            'Create Ad Group': {
                                'AdGroupName': 'Test AdGroup 1',
                                'type': 'DigitalDisplayAdGroupCreate',
                            }
                        },
                    ]
                },
                {
                    'wf_template_name': 'Block - Display Ad Group Setup',
                    'blocks': [
                        {
                            'wf_template_name': 'Block - Display Creative Upload v2',
                            'Creative Upload': {
                                'ClickthroughUrl': 'http://dummy.com',
                                'Creative Name': 'Test Creative 3',
                                'DisplayCreativeType': 'Image Banner or Interstitial',
                                'LandingPageUrl': 'http://dummy.com',
                                'ThirdPartyImpressionTrackingUrl': 'http://dummy.com',
                                'ImageS3URL': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/mobile_banner.png',
                            }
                        },
                        {
                            'wf_template_name': 'Block - Display Create Ad Group',
                            'Create Ad Group': {
                                'AdGroupName': 'Test AdGroup 2',
                                'type': 'DigitalDisplayAdGroupCreate',
                            }
                        },
                    ]
                },
                {
                    'wf_template_name': 'Block - Display QA',
                    'blocks': [
                        {
                            'wf_template_name': 'Block - Display QA Creative v2',
                            'Creative QA': {
                                'ClickthroughUrl': 'http://dummy.com',
                                'Creative Name': 'Test Creative 1',
                                'Creative Size': '300x250',
                                'LandingPageUrl': 'http://dummy.com',
                                'ThirdPartyImpressionTrackingUrl': 'http://dummy.com',
                                'ImageS3URL': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/mobile_banner.png',
                            }
                        },
                        {
                            'wf_template_name': 'Block - Display QA Creative v2',
                            'Creative QA': {
                                'ClickthroughUrl': 'http://dummy.com',
                                'Creative Name': 'Test Creative 2',
                                'Creative Size': '300x250',
                                'LandingPageUrl': 'http://dummy.com',
                                'ThirdPartyImpressionTrackingUrl': 'http://dummy.com',
                                'ImageS3URL': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/mobile_banner.png',
                            }
                        },
                        {
                            'wf_template_name': 'Block - Display QA Ad Group v2',
                            'Ad Group QA': {
                                'AdGroupName': 'Test AdGroup 1',
                                'Campaign Name': 'Test Campaign',
                                'EndDateTimeExclusiveUTC': '2019-05-02T00:00:00.000+0000',
                                'StartDateTimeInclusiveUTC': '2019-04-29T00:00:00.000+0000',
                            }
                        },
                    ]
                },
                {
                    'wf_template_name': 'Block - Display QA',
                    'blocks': [
                        {
                            'wf_template_name': 'Block - Display QA Creative v2',
                            'Creative QA': {
                                'ClickthroughUrl': 'http://dummy.com',
                                'Creative Name': 'Test Creative 3',
                                'Creative Size': '300x250',
                                'LandingPageUrl': 'http://dummy.com',
                                'ThirdPartyImpressionTrackingUrl': 'http://dummy.com',
                                'ImageS3URL': 's3://bridge-file-assets/API_files/orderID_10000129/Channel_2/mobile_banner.png',
                            }
                        },
                        {
                            'wf_template_name': 'Block - Display QA Ad Group v2',
                            'Ad Group QA': {
                                'AdGroupName': 'Test AdGroup 2',
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
