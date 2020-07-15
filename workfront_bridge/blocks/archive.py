from workfront_bridge.blocks.base import WFBlock


class WFArchiveCreativesBlock(WFBlock):
    """Block contains task that will launch archiving of creatives in TTD using ids from
    TTDCreativeID field of custom form.
    """

    template_name = 'Block - Archive Creatives'

    block_params = {
        'Archive Creatives': [
            ('TTDCreativeID', 'ttd_creative_id', False),
            ('TTDAdGroupID', 'ttd_adgroup_id', False),
        ],
    }
