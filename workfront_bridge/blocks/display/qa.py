from workfront_bridge.blocks.base import WFBlock
from workfront_bridge.blocks.display.qa_creative import WFDisplayCreativeQABlock
from workfront_bridge.blocks.display.qa_final_review import WFDisplayQAFinalReviewBlock
from workfront_bridge.exceptions import WFBrigeException


class WFDisplayQABlock(WFBlock):
    """
    @summary: Display QA block
    """

    template_name = 'Block - Display QA'

    def __init__(self):
        super(WFDisplayQABlock, self).__init__(self.template_name)

    def add_creative(self, **kwargs):
        creative = WFDisplayCreativeQABlock()
        for k, v in kwargs.items():
            try:
                getattr(creative, k)
            except AttributeError:
                raise WFBrigeException('Invalid Key: {}'.format(k))
            else:
                setattr(creative, k, v)
        self.append(creative)

    def add_final_review(self, **kwargs):
        final_review = WFDisplayQAFinalReviewBlock()
        for k, v in kwargs.items():
            try:
                getattr(final_review, k)
            except AttributeError:
                raise WFBrigeException('Invalid Key: {}'.format(k))
            else:
                setattr(final_review, k, v)
        self.append(final_review)
