import urllib.parse
from datetime import datetime, timedelta

from .api_responses import LootInfos
from .utils import (
    get_datas,
    API_BASE_URL,
)

class UserLootInfos:

    def __init__(self, username: str) -> None:
        self.name = username.replace('#0', '') if username.endswith('#0') else username
        self.__parsed_name = urllib.parse.quote(self.name)
        datas: LootInfos = get_datas(f"{API_BASE_URL}/loot/{self.__parsed_name}")
        self.__infos = datas['lootInfos']
        self.__last_loot_count = self.__infos[-1]['count']
        self.__last_weekly_loot = self.__infos[-7:]

        # ===== bonus & bonus_when ===== #
        n = 7
        for i in self.__last_weekly_loot[::-1]:
            if i['count'] >= 2000:
                self.bonus = True

                now = datetime.now().date()
                when_days = timedelta(days=n)
                self.bonus_when = now + when_days

                break
            n -= 1
        else:
            self.bonus = False

    @property
    def journa(self) -> bool:
        if self.__last_loot_count == 0: return False
        return True