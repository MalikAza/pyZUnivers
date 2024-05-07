from .utils import FULL_DATE_TIME_FORMAT, DATE_TIME_FORMAT
from datetime import datetime

class Subscription:

    def __init__(self, payload) -> None:
        # checks if payload beginDate and endDate are in format %Y-%m-%dT%H:%M:%S.%f or %Y-%m-%dT%H:%M:%S
        begin_date_format = FULL_DATE_TIME_FORMAT if "." in payload["beginDate"] else DATE_TIME_FORMAT
        end_date_format = FULL_DATE_TIME_FORMAT if "." in payload["endDate"] else DATE_TIME_FORMAT
        self.begin = datetime.strptime(payload["beginDate"], begin_date_format)
        self.end = datetime.strptime(payload["endDate"], end_date_format)