from workfront_bridge.blocks.base import WFBlock


class WFSocialLaunchBlock(WFBlock):
    """
    @summary: Social Setup block. Campaign information.
    """

    template_name = 'Block - Social Launch'

    block_params = {
        'Launch': [
            ('Social Provider', 'provider', True),
        ],
    }

    def __init__(self):
        super(WFSocialLaunchBlock, self).__init__(self.template_name)
        self._set_starter_task(2)
