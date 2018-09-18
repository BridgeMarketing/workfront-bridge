
def datetime_to_wf_format(dt):
    return dt.isoformat().split('.')[0] + '.000+0000'

