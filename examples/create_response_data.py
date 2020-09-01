from workfront.workfront import Workfront
from datetime import datetime as dt
from datetime import timedelta
import json
from workfront_bridge.projects.response_data_builder import \
    ResponseDataBuilder

wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060',
               'thebridgecorp.sb01.workfront.com')

wf.login()

b = ResponseDataBuilder(wf, "Test response data project")

b.set_advertiser('ABC')
b.set_start_date(dt.now().strftime('%Y-%m-%d'))

end_date = dt.now() + timedelta(days=5)
b.set_end_date(end_date.strftime('%Y-%m-%d'))
b.set_selected_product_name('Email Order #1')

reporting_date = dt.now() + timedelta(days=10)
b.set_reporting_date(reporting_date.strftime('%Y-%m-%d'))

b.set_person_ids(json.dumps(['BridgeId']))
b.set_selected_metrics(json.dumps(['SENT', 'OPENED', 'CLICKED']))

b.set_response_flag_format('X/(NULL)')
b.set_output_file_name('output.csv')
b.set_output_file_type('csv')
b.set_output_file_delimiter(',')

b.set_bucket_name('s3bucket')
b.set_prefix('reports')
b.set_aws_access_key('abcdefg1234567')
b.set_aws_secret_key('xyz789')

prj = b.build()

print prj
