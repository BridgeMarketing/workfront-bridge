from workfront_bridge.blocks.base import WFProjectBlock
from workfront_bridge.blocks.base import template_id_from_name


class WFProjectEmailBlock(WFProjectBlock):
    '''
    @summary: Workfront Email Project Block.
    Use this project block to create workfront email projects.
    This project block has no tasks in it but has all the fields of the custom
    forms that an email project should need.
    '''

    template_name = "Base Project Block - Email Channel"

    def __init__(self, wf, prj_name):
        tid = template_id_from_name(wf, self.template_name)
        super(WFProjectEmailBlock, self).__init__(wf, tid, prj_name)

        req = ["ecm_subject"]
        self._set_required_fields(req)

        opt = ["input_html_s3_path"]
        self._set_optional_fields(opt)

        # Project Block fields:
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
