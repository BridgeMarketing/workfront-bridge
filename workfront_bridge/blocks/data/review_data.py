from workfront_bridge.blocks.base import WFBlock


class WFReviewDataBlock(WFBlock):
    """
    @summary: Use this block to add a Review Data task in a data project.
    """

    template_name = 'Block - Data - Review Data V2'


class WFReviewUpdatedDataBlock(WFBlock):
    """
    @summary: Use this block to add the following tasks to a data project:
        * Review Data
        * ReplaceReports in DWH
    """

    template_name = 'Block - Data - Review Updated Data'
