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
            ('ecm_subject', 'email_subject', True),
            ('email_creative_id', 'email_creative_id', True),
            ('tags', 'tags', False),
            ('input_html_s3_path', 'html_s3_path', False),
            ('ecm_from_line', 'from_line', False),
            ('Suppression File Path', 'suppression_file_path', False),
            ('Category', 'category', False),
            ('ecm_live_seed_list', 'live_seed_list', False),
            ('ecm_test_seed_lists', 'test_seed_lists', False),
            ('ecm_html', 'ecm_html', False),
            ('subject_test_prefix', 'subject_test_prefix', False),
        ],
    }

    def __init__(self, prj_name):
        super(WFProjectEmailContainer, self).__init__(self.template_name, name=prj_name)
