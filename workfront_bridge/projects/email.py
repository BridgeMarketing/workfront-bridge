from workfront_bridge.blocks.base import WFProjectContainer
from workfront_bridge.blocks.base import template_id_from_name


class WFProjectEmailContainer(WFProjectContainer):
    '''
    @summary: Workfront Email Project Container.
    Use this project container to create workfront email projects.
    This project container has no tasks in it but has all the fields of the
    custom forms that an email project needs.
    '''

    template_name = "Base Project Container - Email Channel"

    def __init__(self, wf, prj_name):
        tid = template_id_from_name(wf, self.template_name)
        super(WFProjectEmailContainer, self).__init__(wf, tid, prj_name)

        req = ["ecm_subject"]
        self._set_required_fields(req)

        opt = ["input_html_s3_path", "ecm_from_line", "Suppression File Path", "Category", "ecm_live_seed_list",
               "ecm_test_seed_lists"]
        self._set_optional_fields(opt)

        # Project Container fields:
        self._email_subject = None
        self._html_s3_path = None

        self._category = None
        self._from_line = None
        self._suppression_file_path = None
        self._live_seed_list = None
        self._test_seed_lists = None

    @property
    def email_subject(self):
        return self._email_subject

    @email_subject.setter
    def email_subject(self, v):
        self._email_subject = v
        self.set_param_value("ecm_subject", v)

    @property
    def html_s3_path(self):
        return self._html_s3_path

    @html_s3_path.setter
    def html_s3_path(self, v):
        self._html_s3_path = v
        self.set_param_value("input_html_s3_path", v)

    @property
    def from_line(self):
        return self._from_line

    @from_line.setter
    def from_line(self, v):
        self._html_s3_path = v
        self.set_param_value("ecm_from_line", v)

    @property
    def suppression_file_path(self):
        return self._suppression_file_path

    @suppression_file_path.setter
    def suppression_file_path(self, v):
        self._suppression_file_path = v
        self.set_param_value("Suppression File Path", v)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, v):
        self._category = v
        self.set_param_value("Category", v)

    @property
    def live_seed_list(self):
        return self._live_seed_list

    @live_seed_list.setter
    def live_seed_list(self, v):
        self._live_seed_list = v
        self.set_param_value("ecm_live_seed_list", v)

    @property
    def test_seed_lists(self):
        return self._test_seed_lists

    @test_seed_lists.setter
    def test_seed_lists(self, v):
        self._test_seed_lists = v
        self.set_param_value("ecm_test_seed_lists", v)
