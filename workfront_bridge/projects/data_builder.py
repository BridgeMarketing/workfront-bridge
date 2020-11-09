from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.blocks.data.audience import (
    WFAudienceBlock, WFBridgeAudienceBlock, WFClientAudienceBlock,
    WFRetrieveProviderParamsFromDWH, WFRetrieveRetargetingAudience)
from workfront_bridge.blocks.data.hygiene import HygieneDataBlock
from workfront_bridge.blocks.data.merge import MergeDataBlock
from workfront_bridge.blocks.data.review_data import (WFReviewDataBlock,
                                                      WFReviewUpdatedDataBlock)
from workfront_bridge.blocks.data.suppression import (WFSuppressionBlock,
                                                      WFSuppressionGroupBlock)
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.projects.data import WFProjectDataContainer


class DataProjectBuilder(object):
    """
    @summary: Project builder for M&E and B2C projects.
    """

    SUPPRESSION_TYPES = set(["one_per_person", "one_per_household", "one_per_row"])
    IDENTIFIER_FIELDS = set(["bridge_id", "email", "maid", "md5", "postal"])
    SUPPRESSION_FILE_TYPES = IDENTIFIER_FIELDS
    AUDIENCE_FILE_IDENTIFIERS = IDENTIFIER_FIELDS

    def __init__(self, wf, project_name):
        """
        @param wf: Workfront service object
        @param project_name: that the created will have.
        """
        self.project_name = project_name
        self.wf = wf

        self.project_type = None

        # Project
        self.audience_id = None
        self.data_task_id = None
        self.suppression_task_ids = []

        # Blocks
        self.segments = []
        self.suppression_type = None
        self.suppression_files = []

        self.is_audience_updated = False

        self.parent_wf_project_id = None
        self.retargeting_type = None

    def add_audience_segment(self, **kwargs):
        self.segments.append(kwargs)

    def _validate_audience_identifier(self, audience_identifier):
        if audience_identifier not in self.AUDIENCE_FILE_IDENTIFIERS:
            m = "Invalid audience identifier {}. Possible values are {}"
            err = m.format(
                audience_identifier, ",".join(self.AUDIENCE_FILE_IDENTIFIERS)
            )
            raise WFBrigeException(err)

    def add_suppression_file(self, file_path, suppression_file_type):
        """
        @param file_path: s3 file path
        @param suppression_file_type: bridge_id, email, maid, md5, postal
        """
        if suppression_file_type not in self.SUPPRESSION_FILE_TYPES:
            m = "Invalid suppression file type {}. Possible values are {}"
            err = m.format(suppression_file_type, ",".join(self.SUPPRESSION_FILE_TYPES))
            raise WFBrigeException(err)

        kv = {"file_path": file_path, "suppression_file_type": suppression_file_type}
        self.suppression_files.append(kv)
        return self

    def set_suppression_type(self, suppression_type):
        """
        @param suppression_type: one_per_person, one_per_household
        """
        if suppression_type not in self.SUPPRESSION_TYPES:
            m = "Invalid suppression type {}. Possible values are {}"
            raise WFBrigeException(
                m.format(suppression_type, ",".join(self.SUPPRESSION_TYPES))
            )

        self.suppression_type = suppression_type
        return self

    def set_audience_id(self, audience_id):
        self.audience_id = audience_id
        return self

    def set_data_task_id(self, data_task_id):
        self.data_task_id = data_task_id
        return self

    def set_suppression_task_ids(self, suppression_task_ids):
        self.suppression_task_ids = suppression_task_ids
        return self

    def set_is_audience_updated(self, is_audience_updated):
        self.is_audience_updated = is_audience_updated
        return self

    def set_retargeting_data(self, **kwargs):
        self.parent_wf_project_id = kwargs.get("parent_wf_project_id")
        self.retargeting_type = kwargs.get("retargeting_type")

    def _check_viability(self):
        def raise_missing(field_name):
            m = "{} is required for match and export data projects"
            raise WFBrigeException(m.format(field_name))

        for segment in self.segments:
            if (
                segment.get("count_id") is None
                and segment.get("audience_file_path") is None
            ):
                raise WFBrigeException(
                    "{} is required".format("count_id or audience_file_path")
                )
            if segment.get("count_id") is None:
                if segment.get("audience_file_path") is None:
                    raise_missing("audience_file_path")
                if segment.get("audience_name") is None:
                    raise_missing("audience_name")
                if segment.get("audience_identifier") is None:
                    raise_missing("audience_identifier")
                self._validate_audience_identifier(segment["audience_identifier"])
            else:
                if segment["segment_type"] is None:
                    raise_missing("segment_type")

    def build(self):
        """
        @summary: Build the WF project.
        @raise WFBridgeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        """
        self._check_viability()

        project = WFProjectDataContainer(self.project_name)

        project.audience_id = self.audience_id
        project.data_task_id = self.data_task_id
        project.suppression_task_ids = self.suppression_task_ids

        # Specific project blocks
        project.set_data()
        if self.retargeting_type is None:
            is_b2b = False
            group_block = WFAudienceBlock()
            for segment in self.segments:
                if segment.get("segment_type") in ["B2C", "B2B"]:
                    is_b2b = segment.get("segment_type") == "B2B"
                    count_block = WFBridgeAudienceBlock()
                    count_block.count_id = segment.get("count_id")
                    count_block.count_type = segment.get("segment_type")
                    group_block.append(count_block)
                elif segment.get("segment_type") in ["ME", "INSTALL"]:
                    client_block = WFClientAudienceBlock()
                    client_block.segment_type = segment["segment_type"]
                    client_block.audience_file_path = segment["audience_file_path"]
                    client_block.audience_identifier = segment["audience_identifier"]
                    client_block.audience_name = segment["audience_name"]
                    client_block.audience_field_map = segment.get("audience_field_map")
                    group_block.append(client_block)
                else:
                    raise WFBrigeException(
                        "Invalid segment type: {}".format(
                            segment.get("segment_type", "")
                        )
                    )

            if is_b2b:
                project.set_b2b()
            project.append(group_block)
            merge_block = MergeDataBlock()
            project.append(merge_block)
            hygiene_block = HygieneDataBlock()
            project.append(hygiene_block)

            # Suppressions
            if self.suppression_type is not None or len(self.suppression_files) > 0:
                sup_group = WFSuppressionGroupBlock()

                for file_data in self.suppression_files:
                    sup = WFSuppressionBlock()
                    sup.suppression_file_path = file_data["file_path"]
                    sup.suppression_file_type = file_data["suppression_file_type"]
                    sup_group.append(sup)

                if self.suppression_type is not None:
                    sup = WFSuppressionBlock()
                    sup.suppression_type = self.suppression_type
                    sup_group.append(sup)

                project.append(sup_group)
        else:
            project.set_data()
            provider_dwh_block = WFRetrieveProviderParamsFromDWH()
            provider_dwh_block.parent_wf_project_id = self.parent_wf_project_id
            project.append(provider_dwh_block)
            retargeting_block = WFRetrieveRetargetingAudience()
            retargeting_block.retargeting_type = self.retargeting_type
            project.append(retargeting_block)

        # Review
        rev_block = (
            WFReviewUpdatedDataBlock()
            if self.is_audience_updated
            else WFReviewDataBlock()
        )
        project.append(rev_block)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        return wf_project
