import urllib.parse
from datetime import datetime
import pytz

from .banners import UserBanner
from .leaderboards import UserLeaderboards
from .subscription import Subscription
from .overview import UserOverview
from .loot_infos import UserLootInfos
from .challenges import Challenges
from .reputation import UserReputation
from .insomniaque import Insomniaque
from .achievements import Achievements
from .api_responses import AdventCalendar as AdventCalendarType, LootInfos, Base
from .utils import (
    PLAYER_BASE_URL,
    API_BASE_URL,
    get_datas, 
    is_advent_calendar,
    Checker, 
    ADVENT_INDEX
)

class User:
    """ZUniver player various informations
    
    All methods (static or not) make an additional API request"""

    name: str
    """Discord / ZUnivers player username"""

    url: str
    """URL to ZUnivers player page"""

    id: str
    """ZUnivers player identification"""

    discord_id: str
    """Discord user identification"""

    discord_avatar: str
    """URL to Discord user avatar"""

    balance: int
    """a.k.a.: ZUMonnaie"""

    lore_dust: int
    """a.k.a.: Poudre créatrice"""

    lore_fragment: int
    """a.k.a.: Cristal d'histoire"""

    upgrade_dust: int
    """a.k.a.: Eclat d'étoile"""

    rank: int
    """ZUnivers rank name"""

    banner: UserBanner
    """"""

    is_active: bool
    """Is True if the ZUniver player have done
    a command the last 30 days, either False."""

    leaderboards: UserLeaderboards
    """"""

    cards: int
    """Number of cards the player owns"""

    unique_cards: str
    """Number of unique cards the player owns

    format: `unique_cards`/`possible_unique_cards`"""

    unique_golden_cards: str
    """Number of unique golden cards the player owns

    format: `unique_golden_cards`/`possible_unique_golden_cards`"""

    unique_constellation_cards: str
    """Number of unique constellation cards the player owns

    format: `unique_constellation_cards`/`possible_unique_constellation_cards`"""

    unique_golden_constellation_cards: str
    """Number of unique golden constellation cards the player owns

    format: `unique_golden_constellation_cards`/`possible_unique_golden_constellation_cards`"""

    tickets: int
    """Number of tickets the player have scratched"""

    achievements: str
    """Number of achievement the player have done
    
    format: `achievements_done`/`achievements_possible`"""

    subscription: bool|Subscription
    """Informations about the player ZUnivers subscription"""

    tradeless: bool
    """Is True if the player has never made a trade, either False"""

    today_trades: str
    """Number of trades the player have made today
    
    format: `trades_made_today`/`trade_possible_today`"""

    subscription_bonus: str
    """Number of player subscription bonus
    
    format: `subscription_bonus_obtained`/`subscription_bonus_possible`"""

    def __init__(self, username : str) -> None:
        self.name = username.removesuffix('#0')
        self.__parsed_name = urllib.parse.quote(self.name)
        self.__base_infos: Base = get_datas(f"{API_BASE_URL}/user/{self.__parsed_name}")
        self.__user = self.__base_infos['user']
        self.__leaderboards = self.__base_infos['leaderboards']

    @staticmethod
    def get_yearly(username: str, year: int):
        """
        Returns the number of days left for the user to complete a yearful
        looting or False if it's complete.
        """
        return Achievements(username).get_yearly(year)

    @staticmethod
    def get_advent_calendar(username: str):
        """
        Checks if a user has opened their advent calendar for the
        current day.
        """
        username = username.removesuffix('#0')

        parsed_username = urllib.parse.quote(username)
        calendar_datas: AdventCalendarType = get_datas(f"{API_BASE_URL}/calendar/{parsed_username}")
        calendar = calendar_datas["calendars"]
        calendar.sort(key=lambda x: x["index"])

        if len(calendar) == 0: return False

        index_date = int(datetime.now(pytz.timezone('Europe/Paris')).strftime("%d")) - 1
        today_calendar = calendar[index_date]

        return today_calendar["openedDate"] != None

    @staticmethod
    def get_advent_score(username: str) -> int:
        """
        Calculates the advent score for a given username by retrieving
        calendar data and calculating the score based on various criteria.
        """
        username = username.removesuffix('#0')

        parsed_username = urllib.parse.quote(username)
        calendar_datas: AdventCalendarType = get_datas(f"{API_BASE_URL}/calendar/{parsed_username}")
        calendar = calendar_datas['calendars']
        calendar.sort(key=lambda x: x["index"])

        index_date = int(datetime.now(pytz.timezone('Europe/Paris')).strftime("%d"))
        calendar_till_today = calendar[:index_date]

        score = 0
        for calendar in calendar_till_today:
            if calendar['itemMetadata']:
                rarity = f'{calendar["itemMetadata"]["item"]["rarity"]}*'
                if calendar['itemMetadata']['isGolden']: rarity += '+'
                score += ADVENT_INDEX[rarity]
            if calendar['banner']: score += ADVENT_INDEX['banner']
            if calendar['loreDust']: score += ADVENT_INDEX['dust']
            if calendar['loreFragment']: score += ADVENT_INDEX['fragment']
            if calendar['balance']: score += ADVENT_INDEX['balance']
            if calendar['luckyType']: score += ADVENT_INDEX['ticket']

        return score

    @staticmethod
    def get_journa(username: str) -> bool:
        """
        Returns a boolean indicating whether the user
        have done the journa command or not.
        """
        username = username.removesuffix('#0')

        parsed_username = urllib.parse.quote(username)
        loot_datas: LootInfos = get_datas(f"{API_BASE_URL}/loot/{parsed_username}")

        return loot_datas["lootInfos"][364]["count"] != 0

    @staticmethod
    def get_checker(username: str) -> Checker:
        """
        Returns a dictionary of boolean containing information
        about user journa, bonus and advent calendar.
        """
        loot_infos = UserLootInfos(username)

        # advent
        if is_advent_calendar():
            advent = User.get_advent_calendar(username)
        else: advent = None
        
        return {"journa": loot_infos.journa, "bonus": loot_infos.bonus, "advent": advent}

    @staticmethod
    def get_insomniaque(username: str) -> Insomniaque:
        return Insomniaque(username)

    def get_overview(self) -> UserOverview:
        return UserOverview(self.name)
    
    def get_loot_infos(self) -> UserLootInfos:
        return UserLootInfos(self.name)
    
    def get_challenge(self) -> Challenges:
        return Challenges(self.name)
    
    def get_reputation(self) -> UserReputation:
        return UserReputation(self.name)

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
    def subscription(self) -> bool|Subscription:
        sub = self.__base_infos['subscription']

        if not sub: return False
        return Subscription(sub)
    
    @property
    def tradeless(self) -> bool:
        if self.__base_infos['tradeCount'] == 0: return True
        return False
    
    @property
    def today_trades(self) -> str:
        return f"{self.__base_infos['tradeCountToday']}/{self.__base_infos['tradeLimit']}"
    
    @property
    def subscription_bonus(self) -> str:
        return f"{self.__base_infos['subscriptionBonusCount']}/{self.__base_infos['subscriptionBonusLimit']}"