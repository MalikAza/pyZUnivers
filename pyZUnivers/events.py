from api_responses import Event as EventType

from datetime import datetime
from typing import List
from .utils import (
    get_datas,
    API_BASE_URL, 
    FULL_DATE_TIME_FORMAT
)

class Event:
    def __init__(self, payload: EventType) -> None:
        self.__datas = payload

    @property
    def name(self):
        return self.__datas['name']

    @property
    def pack_name(self):
        return self.__datas['pack']['name']

    @property
    def balance_cost(self):
        return self.__datas['balanceCost']
    
    @property
    def dust_cost(self):
        return self.__datas['loreDustCost']
    
    @property
    def is_onetime(self):
        return self.__datas['isOneTime']
    
    @property
    def begin_date(self) -> datetime:
        return datetime.strptime(self.__datas['beginDate'], FULL_DATE_TIME_FORMAT)
    
    @property
    def end_date(self) -> datetime:
        return datetime.strptime(self.__datas['endDate'], FULL_DATE_TIME_FORMAT)
    
    @property
    def is_active(self):
        return self.__datas['isActive']
    

class Events:
    def __init__(self) -> None:
        self.__datas: List[EventType]|[] = get_datas(f"{API_BASE_URL}/event/current")
    
    def get(self) -> List[Event]|[]:
        tmp = []
        for event_payload in self.__datas:
            tmp.append(Event(event_payload))

        return tmp