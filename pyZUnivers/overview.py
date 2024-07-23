from typing import List
from datetime import datetime

from .api_responses import Overview
from .pins import UserPin
from .vortex import Vortex
from .utils import (
    get_datas,
    API_BASE_URL,
    DATE_FORMAT,
    parse_username
)

class UserOverview:
    """
    Reflects a user/overview.

    Attributes:
        name (str): The name of the user.
        pins (List[UserPin]): The pins of the user.
        invocations_before_pity (int): The invocations before pity of the user. (number of cards before a guaranteed rarity four)
        vortex_name (str): The name of the vortex.
        vortex_begin_date (datetime): The begin date of the vortex.
        vortex_end_date (datetime): The end date of the vortex.
        vortex_floor (int): The floor of the user in the vortex.
        vortex_tries (int): The total tries of the user in the vortex.
    """

    def __init__(self, username: str) -> None:
        self.name, self.__parsed_name = parse_username(username)
        self.__infos: Overview = get_datas(f"{API_BASE_URL}/user/{self.__parsed_name}/overview")
        self.__pins = self.__infos['pins']
        self.__vortex_stats = self.__infos['towerStat'] if 'towerStat' in self.__infos else Vortex() # Vortex stats are not always available.

    @property
    def pins(self) -> List[UserPin]:
        return [UserPin(x) for x in self.__pins]
    
    @property
    def invocations_before_pity(self) -> int:
        return int(str(self.__infos['invokeBeforePity'])[:-1])
    
    @property
    def vortex_name(self) -> str:
        if isinstance(self.__vortex_stats, Vortex):
            return self.__vortex_stats.name
        
        return self.__vortex_stats['towerName']
    
    @property
    def vortex_begin_date(self) -> datetime:
        if isinstance(self.__vortex_stats, Vortex):
            return self.__vortex_stats.begin_date

        return datetime.strptime(self.__vortex_stats['towerSeasonBeginDate'], DATE_FORMAT)

    @property
    def vortex_end_date(self) -> datetime:
        if isinstance(self.__vortex_stats, Vortex):
            return self.__vortex_stats.end_date

        return datetime.strptime(self.__vortex_stats['towerSeasonEndDate'], DATE_FORMAT)

    @property
    def vortex_floor(self) -> int:
        if isinstance(self.__vortex_stats, Vortex) or not self.__vortex_stats['maxFloorIndex']:
            return 0
        
        if self.__vortex_stats['maxFloorIndex'] == 0:
            return 1
        
        return self.__vortex_stats['maxFloorIndex'] + 1
    
    @property
    def vortex_tries(self) -> int:
        if isinstance(self.__vortex_stats, Vortex):
            return 0
        
        return self.__vortex_stats['towerLogCount']