from datetime import date, datetime


def datetime_to_wf_format(dt):
    """Transforms a python datetime or date object to a Workfront UTC"""
    if dt is None:
        return None
    if type(dt) == date:
        dt = datetime.combine(dt, datetime.min.time())
    return dt.isoformat().split('.')[0] + '.000+0000'


