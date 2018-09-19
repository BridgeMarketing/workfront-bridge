from workfront_bridge.blocks.base import WFBlock


class CWPushBlock(WFBlock):
    """
    @summary: Single block for CW Push Project.
    """

    template_name = 'Block - CW Push'

    def __init__(self):
        super(CWPushBlock, self).__init__(self.template_name)
