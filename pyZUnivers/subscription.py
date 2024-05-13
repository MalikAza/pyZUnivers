from .utils import get_correct_datetime_format
from datetime import datetime

class Subscription:

    def __init__(self, payload) -> None:
        begin_date_format = get_correct_datetime_format(payload["beginDate"])
        end_date_format = get_correct_datetime_format(payload["endDate"])
        
        self.begin = datetime.strptime(payload["beginDate"], begin_date_format)
        self.end = datetime.strptime(payload["endDate"], end_date_format)