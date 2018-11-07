from workfront_bridge.blocks.base import WFBlock


class WFSocialSetupBlock(WFBlock):
    """
    @summary: Social Setup block. Campaign information.
    """

    template_name = 'Block - Social Setup'
    create_campaign_task_name = 'Create Campaign'

    def __init__(self):
        super(WFSocialSetupBlock, self).__init__(self.template_name)
        self._add_required_parameters([
            'Social Campaign Title',
        ])
        self._add_optional_parameters([
            'FB/Instagram FB Page ID',
            'FB/Instagram IG Account ID',
            'FB/Instagram Advertising Objective',
            'FB/Instagram Offer',
            'FB/Instagram Apply Block List',
        ])
        self._campaign_title = None
        self._fb_page_id = None
        self._fb_ig_acc_id = None
        self._fb_advertising_objective = None
        self._fb_offer = None
        self._fb_apply_block_list = None
        self._set_starter_task(2)

    @property
    def campaign_title(self):
        return self._campaign_title

    @campaign_title.setter
    def campaign_title(self, v):
        self._campaign_title = v
        self.set_parameter(self.create_campaign_task_name, 'Social Campaign Title', v)

    @property
    def fb_page_id(self):
        return self._fb_page_id

    @fb_page_id.setter
    def fb_page_id(self, v):
        self._fb_page_id = v
        self.set_parameter(self.create_campaign_task_name, 'FB/Instagram FB Page ID', v)

    @property
    def fb_ig_acc_id(self):
        return self._fb_ig_acc_id

    @fb_ig_acc_id.setter
    def fb_ig_acc_id(self, v):
        self._fb_ig_acc_id = v
        self.set_parameter(self.create_campaign_task_name, 'FB/Instagram IG Account ID', v)

    @property
    def fb_advertising_objective(self):
        return self._fb_advertising_objective

    @fb_advertising_objective.setter
    def fb_advertising_objective(self, v):
        self._fb_advertising_objective = v
        self.set_parameter(self.create_campaign_task_name, 'FB/Instagram Advertising Objective', v)

    @property
    def fb_offer(self):
        return self._fb_offer

    @fb_offer.setter
    def fb_offer(self, v):
        self._fb_offer = v
        self.set_parameter(self.create_campaign_task_name, 'FB/Instagram Offer', v)

    @property
    def fb_apply_block_list(self):
        return self._fb_apply_block_list

    @fb_apply_block_list.setter
    def fb_apply_block_list(self, v):
        self._fb_apply_block_list = v
        self.set_parameter(self.create_campaign_task_name, 'FB/Instagram Apply Block List', v)

