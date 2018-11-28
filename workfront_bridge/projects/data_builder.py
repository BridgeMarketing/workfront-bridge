from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.exceptions import WFBrigeException
from workfront_bridge.projects.data import WFProjectDataContainer
from workfront_bridge.blocks.data.pull_and_hygine_data import WFPullAndHygieneDataBlock
from workfront_bridge.blocks.data.create_and_export_audience import WFCreatExportAudienceBlock
from workfront_bridge.blocks.data.review_data import WFReviewDataBlock
from workfront_bridge.blocks.data.suppression import WFSuppressionGroupBlock
from workfront_bridge.blocks.data.suppression import WFSuppressionBlock


class DataProjectBuilder(object):
    """
    @summary: Project builder for M&E and B2C projects.
    """

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
        self.count_id

        self.audience_file_path = None
        self.audience_identifier = None
        self.audience_name = None

        self.suppression_type = None
        self.suppression_files = []

        return self

    def set_b2c(self):
        self.project_type = "b2c"
        return self

    def set_match_and_export(self):
        self.project_type = "m&e"
        return self

    #
    # B2c Specific settings
    #
    def set_count_id(self, count_id):
        self.count_id = count_id
        return self
    #
    # END B2c Specific settings
    #

    #
    # Match and Export Specific settings
    #
    def set_audience_file_path(self, audience_file_path):
        self.audience_file_path = audience_file_path
        return self

    def set_audience_name(self, audience_name):
        self.audience_name = audience_name
        return self

    def set_audience_identifier(self, audience_identifier):
        self.audience_identifier = audience_identifier
        return self
    #
    # END Match and Export Specific settings
    #

    #
    # Common settings
    #
    def add_suppression_file(self, file_path, suppression_file_type):
        '''
        @param file_path: s3 file path
        @param supression_type: Bridge ID, Email, MAID, Md5, Postal
        '''
        kv = {
            "file_path": file_path,
            "suppression_file_type": suppression_file_type
        }
        self.supression_files.append(kv)
        return self

    def set_suppression_type(self, suppression_type):
        '''
        @param suppression_type: one_per_persone, one_per_household
        '''
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

    def _check_viability_b2c(self):
        if self.count_id is None:
            raise WFBrigeException("{} is required".format("count_id"))

    def _check_viability_match_and_export(self):
        def raise_missing(field_name):
            m = "{} is required for match and export data projects"
            raise WFBrigeException(m.format(field_name))

        if self.audience_file_path is None:
            raise_missing("audience_file_path")
        if self.audience_name is None:
            raise_missing("audience_name")
        if self.audience_identifier is None:
            raise_missing("audience_identifier")

    def _check_viability(self):
        if self.project_type is None:
            m = "You must specify the type of data project to be created (use"\
                " set_b2c or set_match_and_export)"
            raise WFBrigeException(m)

        if self.project_type == "b2c":
            self._check_viability_b2c()
        elif self.project_type == "m&e":
            self._check_viability_match_and_export()
        else:
            raise Exception("Invalid data project type")

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
        if self.project_type == "b2c":
            project.set_b2c()
            b = WFPullAndHygieneDataBlock()
            b.count_id = self.count_id
            project.append(b)
        elif self.project_type == "m&e":
            project.set_match_and_export()
            project.audience_file_path = self.audience_file_path
            b = WFCreatExportAudienceBlock()
            b.audience_file_path = self.audience_file_path
            b.audience_identifier = self.audience_identifier
            b.audience_name = self.audience_name
            project.append(b)

        # Suppressions
        if self.suppression_type is not None or len(self.suppression_files) > 0:
            sup_group = WFSuppressionGroupBlock()
            project.append(sup_group)

            if self.suppression_type is not None:
                sup = WFSuppressionBlock()
                sup.suppression_type = self.suppression_type
                sup_group.append(sup)

            for file_data in self.suppression_files:
                sup = WFSuppressionBlock()
                sup.suppression_file_path = file_data["file_path"]
                sup.suppression_file_type = file_data["suppression_file_type"]
                sup_group.append(sup)

        # Review
        rev_block = WFReviewDataBlock()
        project.append(rev_block)

        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        return wf_project
