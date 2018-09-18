
def datetime_to_wf_format(dt):
    if dt is None:
        return None
    return dt.isoformat().split('.')[0] + '.000+0000'


