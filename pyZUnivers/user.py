from datetime import datetime
import pytz
from typing import List

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
from .api_responses.items import UserInventoryObject
from .utils import (
    PLAYER_BASE_URL,
    API_BASE_URL,
    get_datas, 
    is_advent_calendar,
    Checker, 
    ADVENT_INDEX,
    get_inventory,
    parse_username,
    best_inventory
)

class User:
    """Represents a ZUnivers player and contains various information about the player.

    All methods (static or not) make an additional API request.

    Attributes:
        url (str): The URL to the ZUnivers player page.
        id (str): The ZUnivers player identification.
        discord_id (str): The Discord user identification.
        discord_avatar (str): The URL to the Discord user avatar.
        balance (int): The amount of ZUMonnaie the player has.
        lore_dust (int): The amount of Poudre créatrice the player has.
        lore_fragment (int): The amount of Cristal d'histoire the player has.
        upgrade_dust (int): The amount of Eclat d'étoile the player has.
        rank (str): The ZUnivers rank name.
        banner (UserBanner): The UserBanner object for the user.
        is_active (bool): True if the ZUniver player have done a command in the last 30 days, False otherwise.
        leaderboards (UserLeaderboards): The UserLeaderboards object for the user.
        cards (int): The number of cards the player owns.
        unique_cards (str): The number of unique cards the player owns. (format: unique_cards/possible_unique_cards)
        unique_golden_cards (str): The number of unique golden cards the player owns. (format: unique_golden_cards/possible_unique_golden_cards)
        unique_constellation_cards (str): The number of unique constellation cards the player owns. (format: unique_constellation_cards/possible_unique_constellation_cards)
        unique_golden_constellation_cards (str): The number of unique golden constellation cards the player owns. (format: unique_golden_constellation_cards/possible_unique_golden_constellation_cards)
        tickets (int): The number of tickets the player have scratched.
        achievements (str): The number of achievements the player have done. (format: achievements_done/achievements_possible)
        subscription (bool|Subscription): The Subscription object for the player if they have one, False otherwise.
        tradeless (bool): True if the player has never made a trade, False otherwise.
        today_trades (str): The number of trades the player have made today. (format: trades_made_today/trade_possible_today)
        subscription_bonus (str): The number of player subscription bonus. (format: subscription_bonus_obtained/subscription_bonus_possible)
    """

    def __init__(self, username : str) -> None:
        self.name, self.__parsed_name = parse_username(username)
        self.__base_infos: Base = get_datas(f"{API_BASE_URL}/user/{self.__parsed_name}")
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
        return self.__user['balance']
    
    @property
    def lore_dust(self) -> int:
        return self.__user['loreDust']
    
    @property
    def lore_fragment(self) -> int:
        return self.__user['loreFragment']
    
    @property
    def upgrade_dust(self) -> int:
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
        sub = self.__base_infos['subscription'] if 'subscription' in self.__base_infos else None

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

    @staticmethod
    def get_yearly(username: str, year: int):
        """
        Returns the number of days left for the user to complete a yearful
        looting or False if it's complete.
        
        Args:
            username (str): The username of the user.
            year (int): The year for which to check the yearly looting.
        
        Returns:
            int|bool: The number of days left for the user to complete the yearly looting,
                      or False if it's already complete.
        """
        return Achievements(username).get_yearly(year)

    @staticmethod
    def get_advent_calendar(username: str):
        """
        Checks if a user has opened their advent calendar for the
        current day.
        
        Args:
            username (str): The username of the user.
        
        Returns:
            bool: True if the user has opened the advent calendar for the current day,
                  False otherwise.
        """
        username, parsed_username = parse_username(username)

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
        
        Args:
            username (str): The username of the user.
        
        Returns:
            int: The advent score for the user.
        """
        username, parsed_username = parse_username(username)

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
        
        Args:
            username (str): The username of the user.
        
        Returns:
            bool: True if the user has done the journa command, False otherwise.
        """
        username, parsed_username = parse_username(username)

        loot_datas: LootInfos = get_datas(f"{API_BASE_URL}/loot/{parsed_username}")

        return loot_datas["lootInfos"][364]["count"] != 0

    @staticmethod
    def get_checker(username: str) -> Checker:
        """
        Returns a dictionary of boolean containing information
        about user journa, bonus and advent calendar.
        
        Args:
            username (str): The username of the user.
        
        Returns:
            dict: A dictionary containing information about user journa, bonus, and advent calendar.
        """
        loot_infos = UserLootInfos(username)

        # advent
        if is_advent_calendar():
            advent = User.get_advent_calendar(username)
        else: advent = None

        now = datetime.now(pytz.timezone('Europe/Paris')).strftime('%Y-%m-%d')

        bonus = loot_infos.bonus
        if not loot_infos.journa and loot_infos.bonus_when.strftime('%Y-%m-%d') == now:
            bonus = False
        
        return {"journa": loot_infos.journa, "bonus": bonus, "advent": advent}

    @staticmethod
    def get_insomniaque(username: str) -> Insomniaque:
        """
        Returns the Insomniaque object for the given username.
        
        Args:
            username (str): The username of the user.
        
        Returns:
            Insomniaque: The Insomniaque object.
        """
        return Insomniaque(username)

    def get_overview(self) -> UserOverview:
        """
        Returns the UserOverview object for the user.
        
        Returns:
            UserOverview: The UserOverview object.
        """
        return UserOverview(self.name)
    
    def get_loot_infos(self) -> UserLootInfos:
        """
        Returns the UserLootInfos object for the user.
        
        Returns:
            UserLootInfos: The UserLootInfos object.
        """
        return UserLootInfos(self.name)
    
    def get_challenge(self) -> Challenges:
        """
        Returns the Challenges object for the user.
        
        Returns:
            Challenges: The Challenges object.
        """
        return Challenges(self.name)
    
    def get_reputation(self) -> UserReputation:
        """
        Returns the UserReputation object for the user.
        
        Returns:
            UserReputation: The UserReputation object.
        """
        return UserReputation(self.name)
    
    def get_inventory(self, search: str = None) -> List[UserInventoryObject]:
        """
        Returns the inventory of the user.
        
        Args:
            search (str, optional): A search query to filter the inventory. Defaults to None.
        
        Returns:
            List[UserInventoryObject]: The inventory of the user.
        """
        return get_inventory(self.__parsed_name, search)
    def best_inventory(self, limit: int = 10) -> List[UserInventoryObject]:
        return best_inventory(self.__parsed_name, limit=limit)