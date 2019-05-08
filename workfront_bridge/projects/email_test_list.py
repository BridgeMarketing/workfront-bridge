from workfront_bridge.blocks.base import WFBlock


class WFProjectEmailTestListContainer(WFBlock):
    '''
    @summary: Workfront Email Test List Project Container.
    Use this project container to create workfront email test lists projects.
    This project container has no tasks in it but has all the fields of the
    custom forms that an email test list project needs.
    '''

    template_name = "Base Project Container - Email Test List"

    block_params = {
        '': [
            ('ecm_subject', 'email_subject', True, lambda x: str(x.encode('utf-8'))),
            ('email_creative_id', 'email_creative_id', True),
            ('input_html_s3_path', 'html_s3_path', False),
            ('ecm_from_line', 'from_line', False),
            ('ecm_test_seed_list', 'test_seed_list', False),
            ('ecm_html', 'ecm_html', False),
            ('subject_test_prefix', 'subject_test_prefix', False),
        ],
    }

    def __init__(self, prj_name):
        super(WFProjectEmailTestListContainer, self).__init__(self.template_name, name=prj_name)
