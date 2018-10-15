from workfront_bridge.blocks.base import WFBlock


class TargetedBonusMediaBlock(WFBlock):
    """
    @summary: Single block for Targeted Bonus Media Project.
    """

    template_name = 'Block - Targeted Bonus Media Channel'

    def __init__(self):
        super(TargetedBonusMediaBlock, self).__init__(self.template_name)
