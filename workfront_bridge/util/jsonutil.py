import json
from datetime import datetime, date


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return o.replace(microsecond=0).isoformat()

        return super(DateTimeEncoder, self).default(o)
