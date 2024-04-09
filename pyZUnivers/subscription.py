from .utils import FULL_DATE_TIME_FORMAT, DATE_TIME_FORMAT
from datetime import datetime

class Subscription:

    def __init__(self, payload) -> None:
        self.begin = datetime.strptime(payload["beginDate"], FULL_DATE_TIME_FORMAT)
        self.end = datetime.strptime(payload["endDate"], DATE_TIME_FORMAT)