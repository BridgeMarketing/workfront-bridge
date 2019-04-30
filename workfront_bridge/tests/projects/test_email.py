import mock
from datetime import datetime
from dateutil import tz

from workfront_bridge.tests.projects.base import BaseBuilderTest
from workfront_bridge.projects import email_builder


class Test_Email_Builder(BaseBuilderTest):
    def setUp(self):
        super(Test_Email_Builder, self).setUp()

        self.wf = mock.MagicMock()
        self.builder = email_builder.EmailProjectBuilder(self.wf, "Test pablo email project builder 1")

    @mock.patch('workfront_bridge.projects.email_builder.datetime')
    def test_email(self, _datetime):
        dt = datetime(2020, 2, 3, 14, 29, 22, 0, tz.tzutc())
        _datetime.utcnow = mock.Mock(return_value=dt)

        self.builder.add_test_list("s3://some/testlist1.csv")
        self.builder.add_test_list("s3://some/testlist2.csv")
        self.builder.add_test_list("s3://some/testlist2.csv")

        self.builder.set_html("s3://some/creative.html")

        self.builder.set_deployment_datetime(dt)
        self.builder.set_seed_list("s3://some/seed.csv")

        self.builder.set_subject("asuntoooo")
        self.builder.set_send_validate_test_seed_emails(True)

        self.builder.set_audience_provider("ActOn")
        self.builder.set_audience_sender_email("audience_sender@email.com")
        self.builder.set_audience_sender_name("Sender NAME")

        self.builder.set_seeds_provider("Jango")
        self.builder.set_seeds_sender_email("seedssender@email.com")
        self.builder.set_seeds_sender_name("Seed Name")

        self.builder.set_live_seeds_provider("Jango")
        self.builder.set_live_seeds_sender_email("liveseedssender@email.com")
        self.builder.set_live_seeds_sender_name("Live Seed Name")

        self.builder.set_email_creative_id("10")

        prj = self.builder.build()

        expected = {
            "wf_template_name": "Base Project Container - Email Channel",
            "": {
                "email_creative_id": "10",
                "input_html_s3_path": "s3://some/creative.html",
                "ecm_from_line": "Sender NAME",
                "ecm_subject": "asuntoooo",
            },
            "blocks": [
                {
                    "wf_template_name": "Block - Email Validate Html",
                    "Validate HTML": {
                        "ecm_email_subject": "asuntoooo",
                    },
                },
                {
                    "wf_template_name": "Block - Email Test Setup",
                    "Test Setup": {
                        "cm_test_aud_s3_path": "s3://some/testlist1.csv",
                    },
                    "Push to provider": {
                        "SelectedProvider": "Jango",
                        "isTest": "yes",
                    },
                    "Create Flight": {
                        "Campaign Name": "Test List - Test pablo email project builder 1",
                        "Sender Name": "Seed Name",
                        "Deployment Date/Time": "2020-02-03T14:29:22.000+0000",
                        "Sender Email": "seedssender@email.com",
                    },
                },
                {
                    "wf_template_name": "Block - Email Test Setup",
                    "Test Setup": {
                        "cm_test_aud_s3_path": "s3://some/testlist2.csv",
                    },
                    "Push to provider": {
                        "SelectedProvider": "Jango",
                        "isTest": "yes",
                    },
                    "Create Flight": {
                        "Campaign Name": "Test List - Test pablo email project builder 1",
                        "Sender Name": "Seed Name",
                        "Deployment Date/Time": "2020-02-03T14:29:22.000+0000",
                        "Sender Email": "seedssender@email.com",
                    },
                },
                {
                    "wf_template_name": "Block - Email Test Setup",
                    "Test Setup": {
                        "cm_test_aud_s3_path": "s3://some/testlist2.csv",
                    },
                    "Push to provider": {
                        "SelectedProvider": "Jango",
                        "isTest": "yes",
                    },
                    "Create Flight": {
                        "Campaign Name": "Test List - Test pablo email project builder 1",
                        "Sender Name": "Seed Name",
                        "Deployment Date/Time": "2020-02-03T14:29:22.000+0000",
                        "Sender Email": "seedssender@email.com",
                    },
                },
                {
                    "wf_template_name": "Block - Email Live Setup v3",
                    "Push to provider": {
                        "SelectedProvider": "Jango",
                    },
                    "Live Setup": {
                        "live_seed_list_s3_path": "s3://some/seed.csv",
                    },
                    "Create Flight": {
                        "Campaign Name": "Live List - Test pablo email project builder 1",
                        "Sender Name": "Live Seed Name",
                        "Deployment Date/Time": "2020-02-03T14:29:22.000+0000",
                        "Sender Email": "liveseedssender@email.com",
                    }
                },
                {
                    "wf_template_name": "Block - Email Audience Live Setup v2",
                    "Push to provider": {
                        "SelectedProvider": "ActOn",
                    },
                    "Create Flight": {
                        "Campaign Name": "Test pablo email project builder 1",
                        "Sender Name": "Sender NAME",
                        "Deployment Date/Time": "2020-02-03T14:29:22.000+0000",
                        "Sender Email": "audience_sender@email.com",
                    },
                },
                {
                    "wf_template_name": "Block - Email Review Deployment",
                }
            ],
        }

        self.assertDeepEquals(expected, prj)
