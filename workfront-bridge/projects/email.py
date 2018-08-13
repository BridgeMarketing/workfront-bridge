from workfront-bridge.blocks.base import WFProjectBlock
from workfront-bridge.exceptions import WFBrigeException
from workfront-bridge.blocks.email import WFEmailTestSeedBlockNoEmailSent


class WFProjectEmailBlock(WFProjectBlock):
    
    template_name = "Base Project Block - Email Channel"
    
    def __init__(self, wf, prj_name):
        super(WFProjectEmailBlock, self).__init__(wf, prj_name)
        self.test_seed_list = []
        self.live_seed_list = None
        self.email_subject = None
        self.zip_s3_path = None
        self.html_s3_path = None

        req = ["ecm_subject", ]
        self._set_required_fields(req):

        opt = ["input_html_s3_path"]
        self._set_optional_fields(opt):

    def _check_param_values(self):
        super(WFProjectEmailBlock, self)._check_param_values()
        if self.zip_s3_path is None and self.html_s3_path is None:
            err += "At least a zip or an html should be provided"
            raise  WFBrigeException(err)

    def build(self):
        
        for test_list_path in self.test_seed_list:
            b = WFEmailTestSeedBlockNoEmailSent(wf)
            b.seed_list_s3_path = test_list_path