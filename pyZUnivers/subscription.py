from .utils import FULL_DATE_FORMAT
from datetime import datetime

class Subscription:

    def __init__(self, payload) -> None:
        self.begin = datetime.strptime(payload["beginDate"], FULL_DATE_FORMAT)
        self.end = datetime.strptime(payload["endDate"], FULL_DATE_FORMAT)