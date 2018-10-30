from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.blocks.display.qa_creative import WFDisplayCreativeQABlock
from workfront_bridge.blocks.display.qa_final_review import WFDisplayQAFinalReviewBlock
from workfront_bridge.tools import set_kwargs


class WFDisplayQABlock(WFBlock):
    """
    @summary: Display QA block
    """

    template_name = 'Block - Display QA'

    def __init__(self):
        super(WFDisplayQABlock, self).__init__(self.template_name)

    def add_creative(self, **kwargs):
        creative = WFDisplayCreativeQABlock()
        creative = set_kwargs(creative, kwargs)
        self.append(creative)

    def add_final_review(self, **kwargs):
        final_review = WFDisplayQAFinalReviewBlock()
        final_review = set_kwargs(final_review, kwargs, exclude=['creatives'])
        self.append(final_review)

