from workfront_bridge.blocks.base import WFBlock


class WFProjectEmailContainer(WFBlock):
    '''
    @summary: Workfront Email Project Container.
    Use this project container to create workfront email projects.
    This project container has no tasks in it but has all the fields of the
    custom forms that an email project needs.
    '''

    template_name = "Base Project Container - Email Channel"

    block_params = {
        '': [
            ('ecm_subject', 'email_subject', True, lambda x: str(x.encode('utf-8'))),
            ('subject_test_prefix', 'subject_test_prefix', False, lambda x: str(x.encode('utf-8'))),
            ('email_creative_id', 'email_creative_id', True),
            ('tags', 'tags', False),
            ('input_html_s3_path', 'html_s3_path', False),
            ('ecm_from_line', 'from_line', True, lambda x: str(x.encode('utf-8'))),
            ('Suppression File Path', 'suppression_file_path', False),
            ('Category', 'category', False),
            ('ecm_live_seed_list', 'live_seed_list', False),
            ('ecm_html', 'ecm_html', False),
            ('ttd_advertiser_id', 'ttd_advertiser_id', False),
            ('ttd_bonus_media_advertiser_id', 'ttd_bonus_media_advertiser_id', False),
            ('lr_account_id', 'lr_account_id', False),
            ('lr_bonus_media_account_id', 'lr_bonus_media_account_id', False),
            ('deployment_time', 'deployment_time', False),
            ('project_id', 'project_id', False),
        ],
    }

    def __init__(self, prj_name):
        super(WFProjectEmailContainer, self).__init__(self.template_name, name=prj_name)
