from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.blocks.archive import WFArchiveCreativesBlock
from workfront_bridge.blocks.display.ad_group_creative_upload import WFDisplayCreativeUploadBlock
from workfront_bridge.blocks.display.ad_group_create import WFDisplayCreateAdGroupBlock
from workfront_bridge.tools import set_kwargs


class WFDisplayAdGroupSetupBlock(WFBlock):
    """
    @summary: Display Ad Group Setup block
    """

    template_name = 'Block - Display Ad Group Setup'

    def add_creative(self, **kwargs):
        block_class = kwargs.pop('block_class', WFDisplayCreativeUploadBlock)
        creative = block_class()
        creative = set_kwargs(creative, kwargs)
        self.append(creative)

    def add_ad_group(self, **kwargs):
        block_class = kwargs.pop('block_class', WFDisplayCreateAdGroupBlock)
        ad_group = block_class()
        ad_group = set_kwargs(ad_group, kwargs, exclude=['creatives'])
        self.append(ad_group)

    def archive_creative(self, **kwargs):
        block_class = kwargs.pop('block_class', WFArchiveCreativesBlock)
        archive_block = block_class()
        archive_block = set_kwargs(archive_block, kwargs)
        self.append(archive_block)

    def update_ad_group(self, **kwargs):
        block_class = kwargs.pop('block_class', WFUpdateAdGroupBlock)
        update_block = block_class()
        update_block = set_kwargs(update_block, kwargs)
        self.append(update_block)


class WFUpdateAdGroupBlock(WFBlock):
    """Block contains task that will hit TTD's AdGroup endpoint with custom payload."""

    template_name = 'Block - Update Ad Group'

    block_params = {
        'Update Ad Group': [
            ('data_update', 'payload', ''),
        ],
    }
