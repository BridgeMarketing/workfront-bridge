from workfront_bridge.blocks.base import WFBlock


class WFEmailResponseDataContainer(WFBlock):
    """
    @summary: Email Response Data block
    """

    template_name = 'Email Response Data'

    block_params = {
        '': [
            ('advertiser', 'advertiser', True),
            ('selected_product_name', 'selected_product_name', True),
            ('start_date', 'start_date', True),
            ('end_date', 'end_date', True),
            ('reporting_date', 'reporting_date', True),
            ('person_ids', 'person_ids', True),
            ('selected_metrics', 'selected_metrics', True),
            ('response_flag_format', 'response_flag_format', True),
            ('output_file_name', 'output_file_name', True),
            ('output_file_type', 'output_file_type', True),
            ('output_file_delimiter', 'output_file_delimiter', True),
            ('bucket_name', 'bucket_name', False),
            ('prefix', 'prefix', False),
            ('aws_access_key', 'aws_access_key', False),
            ('aws_secret_key', 'aws_secret_key', False),
            ('sftp_url', 'sftp_url', False),
            ('sftp_port', 'sftp_port', False),
            ('sftp_directory', 'sftp_directory', False),
            ('sftp_username', 'sftp_username', False),
            ('sftp_password', 'sftp_password', False),
        ],
    }

    def __init__(self, project_name):
        super(WFEmailResponseDataContainer, self).__init__(self.template_name,
                                                           name=project_name)
