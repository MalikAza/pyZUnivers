from datetime import datetime, timedelta, date

import pytz

from .api_responses import LootInfos, LootType
from .errors import UserNotFound
from .utils import (
    ResourceNotFoundError,
    get_datas,
    API_BASE_URL,
    parse_username
)

class LastBonusTooFarError(Exception):
    def __str__(self) -> str:
        return f'The last bonus is too far away (364+ days) to predict the next one.'

class UserLootInfos:
    """
    Reflects the loot infos of a user.

    Attributes:
        name (str): The name of the user.
        bonus (bool): If the user has the bonus.
        bonus_when (date): When the user will have the bonus.
        journa (bool): If the user has the journa.
    """

    def __init__(self, username: str) -> None:
        self.name, self.__parsed_name = parse_username(username)
        try:
            datas: LootInfos = get_datas(f"{API_BASE_URL}/loot/{self.__parsed_name}")
        except ResourceNotFoundError:
            raise UserNotFound(self.name)
        
        self.loot_infos = datas

    def __today_key(self) -> str:
        return datetime.now(pytz.timezone('Europe/Paris')).strftime("%Y-%m-%d")
    
    def __days_before_key(self, days_before: int) -> str:
        today = datetime.now(pytz.timezone('Europe/Paris'))
        delta = timedelta(days=days_before)
        datetime_before = today - delta

        return datetime_before.strftime("%Y-%m-%d")
    
    def __is_today_key_presents(self) -> bool:
        return self.__today_key() in self.loot_infos.keys()
    
    def __is_loot_type_present_in_day(self, loot_type: LootType, day: str) -> bool:
        loots_day = self.loot_infos.get(day)

        for loot in loots_day:
            if loot["type"] == loot_type.value:
                return True
            
        return False
    
    def __daily_count_since_last_weekly(self) -> int:
        daily_count = 0

        for days_ago in range(len(self.loot_infos)):
            day_key = self.__days_before_key(days_ago)

            if day_key not in self.loot_infos: continue

            if self.__is_loot_type_present_in_day(LootType.WEEKLY, day_key):
                break

            if self.__is_loot_type_present_in_day(LootType.DAILY, day_key):
                daily_count += 1

        return daily_count
    
    def __last_day_looted(self) -> datetime:
        for days_ago in range(len(self.loot_infos)):
            day_key = self.__days_before_key(days_ago)

            if day_key in self.loot_infos:
                return datetime.strptime(day_key, '%Y-%m-%d')

    @property
    def bonus(self) -> bool:
        return not (self.__daily_count_since_last_weekly() >= 7)

    @property
    def bonus_when(self) -> datetime:
        when_days = timedelta(days= 7 - self.__daily_count_since_last_weekly())

        return self.__last_day_looted() + when_days

    @property
    def journa(self) -> bool:
        if not self.__is_today_key_presents(): return False

        return self.__is_loot_type_present_in_day(LootType.DAILY, self.__today_key())