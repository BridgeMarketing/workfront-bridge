from workfront_bridge.blocks.base import WFBlock


class WFDisplayQABlock(WFBlock):
    """
    @summary: Display QA block
    """

    template_name = 'Block - Display QA'

    def __init__(self):
        super(WFDisplayQABlock, self).__init__(self.template_name)
