from datetime import date, datetime
from workfront_bridge.exceptions import WFBrigeException


def datetime_to_wf_format(dt):
    """Transforms a python datetime or date object to a Workfront UTC"""
    if dt is None:
        return None
    if type(dt) == date:
        dt = datetime.combine(dt, datetime.min.time())
    return dt.isoformat().split('.')[0] + '.000+0000'


def set_kwargs(obj, kwargs, exclude=[]):
    """If the argument exists in the object, it is set to the value in
    the kwargs dict.
    Excluded values are ignored.
    """
    for k, v in kwargs.items():
        if k in exclude:
            continue
        try:
            getattr(obj, k)
        except AttributeError:
            raise WFBrigeException('Invalid Key: {}'.format(k))
        else:
            setattr(obj, k, v)
    return obj
