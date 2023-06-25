import urllib.parse
from .banners import UserBanner
from .leaderboards import UserLeaderboards
from .subscription import Subscription
from .overview import UserOverview
from .loot_infos import UserLootInfos
from .utils import (
    PLAYER_BASE_URL,
    API_BASE_URL,
    get_datas
)

class User:

    def __init__(self, username : str) -> None:
        self.name = username.replace('#0', '') if username.endswith('#0') else username
        self.__parsed_name = urllib.parse.quote(self.name)
        self.__base_infos = get_datas(f"{API_BASE_URL}/user/{self.__parsed_name}")
        self.__user = self.__base_infos['user']
        self.__leaderboards = self.__base_infos['leaderboards']

    @property
    def url(self) -> str:
        return f"{PLAYER_BASE_URL}/{self.__parsed_name}"
    
    @property
    def id(self) -> str:
        return self.__user['id']
    
    @property
    def discord_id(self) -> str:
        return self.__user['discordId']
    
    @property
    def discord_avatar(self) -> str:
        return self.__user['discordAvatar']
    
    @property
    def balance(self) -> int:
        """a.k.a.: ZUMonnaie"""
        return self.__user['balance']
    
    @property
    def lore_dust(self) -> int:
        """a.k.a.: Poudre créatrice"""
        return self.__user['loreDust']
    
    @property
    def lore_fragment(self) -> int:
        """a.k.a.: Cristal d'histoire"""
        return self.__user['loreFragment']
    
    @property
    def upgrade_dust(self) -> int:
        """a.k.a.: Eclat d'étoile"""
        return self.__user['upgradeDust']
    
    @property
    def rank(self) -> str:
        return self.__user['rank']['name']
    
    @property
    def banner(self) -> UserBanner:
        return UserBanner(self.__user['userBanner'])
    
    @property
    def is_active(self) -> bool:
        return self.__user['isActive']
    
    @property
    def leaderboards(self) -> UserLeaderboards:
        return UserLeaderboards(self.__leaderboards)
    
    @property
    def cards(self) -> int:
        return self.__base_infos['inventoryCount']
    
    @property
    def unique_cards(self) -> str:
        return f"{self.__base_infos['inventoryUniqueCount']}/{self.__base_infos['itemCount']}"
    
    @property
    def unique_golden_cards(self) -> str:
        return f"{self.__base_infos['inventoryUniqueGoldenCount']}/{self.__base_infos['itemCount']}"
    
    @property
    def unique_constellation_cards(self) -> str:
        return f"{self.__base_infos['inventoryUniqueUpgradableCount']}/{self.__base_infos['upgradableItemCount']}"
    
    @property
    def unique_golden_constellation_cards(self) -> str:
        return f"{self.__base_infos['inventoryUniqueGoldenUpgradableCount']}/{self.__base_infos['upgradableItemCount']}"
    
    @property
    def tickets(self) -> int:
        return self.__base_infos['luckyCount']
    
    @property
    def achievements(self) -> str:
        return f"{self.__base_infos['achievementLogCount']}/{self.__base_infos['achievementCount']}"
    
    @property
    def subscription(self):
        sub = self.__base_infos['subscription']

        if not sub: return False
        return Subscription(sub)
    
    @property
    def tradeless(self):
        if self.__base_infos['tradeCount'] == 0: return True
        return False
    
    @property
    def today_trades(self) -> str:
        return f"{self.__base_infos['tradeCountToday']}/{self.__base_infos['tradeLimit']}"
    
    @property
    def subscription_bonus(self) -> str:
        return f"{self.__base_infos['subscriptionBonusCount']}/{self.__base_infos['subscriptionBonusLimit']}"
    
    def get_overview(self) -> UserOverview:
        return UserOverview(self.name)
    
    def get_loot_infos(self) -> UserLootInfos:
        return UserLootInfos(self.name)