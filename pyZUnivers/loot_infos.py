import urllib.parse
from datetime import datetime, timedelta
import pytz

from .api_responses import LootInfos
from .utils import (
    get_datas,
    API_BASE_URL,
)

class UserLootInfos:

    def __init__(self, username: str) -> None:
        self.name = username.removesuffix('#0')
        self.__parsed_name = urllib.parse.quote(self.name)
        datas: LootInfos = get_datas(f"{API_BASE_URL}/loot/{self.__parsed_name}")
        loot_infos = datas['lootInfos']
        self.__last_loot_count = loot_infos[-1]['count']

        # ===== bonus & bonus_when ===== #
        last_loots = loot_infos[::-1]
        for index, loot in enumerate(last_loots):
            if loot['count'] >= 2000:
                bonus_index = index
                break

        last_bonus = last_loots[:bonus_index]
        self.__journa_count = 0
        for loot in last_bonus:
            if loot['count'] == 0: continue
            self.__journa_count += 1

    @property
    def bonus(self) -> bool:
        return not self.__journa_count == 7

    @property
    def bonus_when(self) -> '_Date':
        now = datetime.now(pytz.timezone('Europe/Paris')).date()
        when_days = timedelta(days=7-self.__journa_count)

        return now + when_days

    @property
    def journa(self) -> bool:
        if self.__last_loot_count == 0: return False
        return True