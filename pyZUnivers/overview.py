import urllib.parse
from typing import List
from datetime import datetime

from api_responses import Overview
from .pins import UserPin
from .utils import (
    get_datas,
    API_BASE_URL,
    DATE_FORMAT
)

class UserOverview:

    def __init__(self, username: str) -> None:
        self.name = username.removesuffix('#0')
        self.__parsed_name = urllib.parse.quote(self.name)
        self.__infos: Overview = get_datas(f"{API_BASE_URL}/user/{self.__parsed_name}/overview")
        self.__pins = self.__infos['pins']
        self.__vortex_stats = self.__infos['towerStat']

    @property
    def pins(self) -> List[UserPin]:
        return [UserPin(x) for x in self.__pins]
    
    @property
    def invocations_before_pity(self) -> int:
        return int(str(self.__infos['invokeBeforePity'])[:-1])
    
    @property
    def vortex_name(self) -> str:
        return self.__vortex_stats['towerName']
    
    @property
    def vortex_begin_date(self) -> datetime:
        return datetime.strptime(self.__vortex_stats['towerSeasonBeginDate'], DATE_FORMAT)

    @property
    def vortex_end_date(self) -> datetime:
        return datetime.strptime(self.__vortex_stats['towerSeasonEndDate'], DATE_FORMAT)

    @property
    def vortex_floor(self) -> int:
        if not self.__vortex_stats or not self.__vortex_stats['maxFloorIndex']:
            return 0
        if self.__vortex_stats['maxFloorIndex'] == 0:
            return 1
        return self.__vortex_stats['maxFloorIndex'] + 1
    
    @property
    def vortex_tries(self) -> int:
        if not self.__vortex_stats:
            return 0
        return self.__vortex_stats['towerLogCount']