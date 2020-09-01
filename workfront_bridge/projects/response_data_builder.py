from dateutil import tz
from workfront.objects.template_project import WFTemplateProject

from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.exceptions import WFBrigeException
from response_data import WFEmailResponseDataContainer


class ResponseDataBuilder(object):
    '''
    @summary: Email project builder to easily construct email workfront
    projects.
    '''

    def __init__(self, wf, project_name):
        '''
        @param wf: Workfront service object
        @param project_name: that the created will have.
        '''
        self.wf = wf
        self.project_name = project_name
        self.orderId = None
        self.account = None
        self.advertiser = None
        self.start_date = None
        self.end_date = None

        self.wf_program_id = None
        self.selected_product_name = None
        self.reporting_date = None

        self.person_ids = None
        self.selected_metrics = None

        self.response_flag_format = None
        self.output_file_name = None
        self.output_file_type = None
        self.output_file_delimiter = None

        self.bucket_name = None
        self.prefix = None
        self.aws_access_key = None
        self.aws_secret_key = None

        self.sftp_url = None
        self.sftp_port = None
        self.sftp_directory = None
        self.sftp_username = None
        self.sftp_password = None

    def set_orderId(self, v):
        self.orderId = v
        return self

    def set_account(self, v):
        self.account = v
        return self

    def set_advertiser(self, v):
        self.advertiser = v
        return self

    def set_start_date(self, v):
        self.start_date = v
        return self

    def set_end_date(self, v):
        self.end_date = v
        return self

    def set_wf_program_id(self, v):
        self.wf_program_id = v
        return self

    def set_selected_product_name(self, v):
        self.selected_product_name = v
        return self

    def set_reporting_date(self, v):
        self.reporting_date = v
        return self

    def set_person_ids(self, v):
        self.person_ids = v
        return self

    def set_selected_metrics(self, v):
        self.selected_metrics = v
        return self

    def set_response_flag_format(self, v):
        self.response_flag_format = v
        return self

    def set_output_file_name(self, v):
        self.output_file_name = v
        return self

    def set_output_file_type(self, v):
        self.output_file_type = v
        return self

    def set_output_file_delimiter(self, v):
        self.output_file_delimiter = v
        return self

    def set_bucket_name(self, v):
        self.bucket_name = v
        return self

    def set_prefix(self, v):
        self.prefix = v
        return self

    def set_aws_access_key(self, v):
        self.aws_access_key = v
        return self

    def set_aws_secret_key(self, v):
        self.aws_secret_key = v
        return self

    def set_sftp_url(self, v):
        self.sftp_url = v
        return self

    def set_sftp_port(self, v):
        self.sftp_port = v
        return self

    def set_sftp_directory(self, v):
        self.sftp_directory = v
        return self

    def set_sftp_username(self, v):
        self.sftp_username = v
        return self

    def set_sftp_password(self, v):
        self.sftp_password = v
        return self

    def build(self):
        '''
        @summary: According to all the parameters set to the builder, build a
        workfront project.
        @raise WFBrigeException: if the combination of parameters set in the
        builder are not compatible (like missing parameters).
        @return: a WFProject object.
        '''

        project = WFEmailResponseDataContainer(self.project_name)
        project.orderId = self.orderId
        project.account = self.account
        project.advertiser = self.advertiser
        project.start_date = self.start_date
        project.end_date = self.end_date

        project.wf_program_id = self.wf_program_id
        project.selected_product_name = self.selected_product_name
        project.reporting_date = self.reporting_date

        project.person_ids = self.person_ids
        project.selected_metrics = self.selected_metrics

        project.response_flag_format = self.response_flag_format
        project.output_file_name = self.output_file_name
        project.output_file_type = self.output_file_type
        project.output_file_delimiter = self.output_file_delimiter

        project.bucket_name = self.bucket_name
        project.prefix = self.prefix
        project.aws_access_key = self.aws_access_key
        project.aws_secret_key = self.aws_secret_key

        project.sftp_url = self.sftp_url
        project.sftp_port = self.sftp_port
        project.sftp_directory = self.sftp_directory
        project.sftp_username = self.sftp_username
        project.sftp_password = self.sftp_password
        
        parser = WFBlockParser(self.wf)
        wf_project = parser.create(project)

        return wf_project
