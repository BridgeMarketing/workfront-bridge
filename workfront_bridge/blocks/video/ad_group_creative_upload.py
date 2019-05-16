from workfront_bridge.blocks.audio.ad_group_creative_upload import WFAudioCreativeUploadBlock


class WFVideoCreativeUploadBlock(WFAudioCreativeUploadBlock):
    """
    @summary: Video Creative Upload block
    """

    def __init__(self):
        super(WFVideoCreativeUploadBlock, self).__init__(self.template_name)
        self.automation_type = 'VideoCreativeUpload'
