from .api_responses import Event as EventType

from datetime import datetime
from typing import List
from .utils import (
    get_datas,
    API_BASE_URL, 
    get_correct_datetime_format
)

class Event:
    """
    A current Event.

    Attributes:
        name (str): The name of the event.
        pack_name (str): The name of the pack for this event.
        balance_cost (int): The balance cost of the event.
        dust_cost (int): The lore dust cost of the event.
        is_onetime (bool): If the event is one time.
        begin_date (datetime): The begin date of the event.
        end_date (datetime): The end date of the event.
        is_active (bool): If the event is active.
    """
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
        datetime_format = get_correct_datetime_format(self.__datas['beginDate'])
        return datetime.strptime(self.__datas['beginDate'], datetime_format)
    
    @property
    def end_date(self) -> datetime:
        datetime_format = get_correct_datetime_format(self.__datas['endDate'])
        return datetime.strptime(self.__datas['endDate'], datetime_format)
    
    @property
    def is_active(self):
        return self.__datas['isActive']
    

class Events:
    """
    All current events.
    """
    def __init__(self) -> None:
        self.__datas: List[EventType]|List = get_datas(f"{API_BASE_URL}/event/current")
    
    def get(self) -> List[Event]|List:
            """
            Retrieves a list of Event objects.

            Returns:
                List[Event]: A list of Event objects.
            """
            tmp = []
            for event_payload in self.__datas:
                tmp.append(Event(event_payload))

            return tmp
