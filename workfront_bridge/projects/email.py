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

        opt = ["input_html_s3_path"]
        self._set_optional_fields(opt)

        # Project Container fields:
        self._email_subject = None
        self._html_s3_path = None

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
