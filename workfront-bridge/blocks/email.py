from workfront-bridge.blocks.base import WFBlock, template_id_from_name


class WFEmailTestSeedBlockNoEmailSent(WFBlock):

    template_name = 'Block - Email Test Setup (no emails sent)'

    def __init__(self, wf):
        template_id = template_id_from_name(wf, self.template_name)
        super(WFEmailProjectBlock, self).__init__(wf, template_id)

        req = ["cm_test_aud_s3_path"]
        self._set_required_fields(req)

    @property
    def seed_list_s3_path(self):
        return self._seed_list_path

    @seed_list_s3_path.setter
    def seed_list_s3_path(self, sl):
        self._seed_list_path = sl
        self.set_task_param_value("Test Setup", "cm_test_aud_s3_path", sl)


# class WFEmailTestSeedBlock(WFEmailTestSeedBlock):
# 
#     template_name = 'Block - Email Test Setup'
# 
#     def __init__(self, wf):
#         super(WFEmailTestSeedBlockNoEmailSent, self).__init__(wf, template_id)
#         template_id = template_id_from_name(wf, prj_name)
#         self.wf_template_id = template_id #  Override template id 
# 
#         req = ["cm_test_aud_s3_path", "Campaign Name", "Sender Name",
#                "Deployment Date/Time", "Sender Email"]
#         self._set_required_fields(req)
# 
#         opt = ["SelectedProvider"]
#         self._set_optional_fields(opt)
