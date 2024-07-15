from typing import List

from .api_responses import (
    UserCorporation as UserCorporationAPIResponse,
    CorporationSummary,
    Corporation as CorporationAPIResponse,
    CorporationBonus,
    CorporationLedger,
    CorporationUser as CorporationUserAPIResponse
)

from datetime import datetime
from .utils import (
    API_BASE_URL,
    get_correct_datetime_format,
    get_datas
)

class UserCorporation:
    """
    Represents the user's corporation.
    
    Attributes:
        id (str): The ID of the corporation.
        name (str): The name of the corporation.
        description (str): The description of the corporation.
        balance (int): The balance of the corporation.
        logo_url (str): The URL of the corporation's logo.
        logo_file_name (str): The file name of the corporation's logo.
        created_date (datetime): The created date of the corporation.
        modified_date (datetime): The modified date of the corporation.
        joined_date (datetime): The joined date of the user in the corporation.
        role (str): The role of the user in the corporation.
        url (str): The URL of the corporation.
    """

    def __init__(self, payload: UserCorporationAPIResponse) -> None:
        self.__payload = payload
        self.__corporation = payload['corporation']

    @property
    def id(self) -> str:
        return self.__corporation['id']
    
    @property
    def name(self) -> str:
        return self.__corporation['name']
    
    @property
    def description(self) -> str:
        return self.__corporation['description']
    
    @property
    def balance(self) -> int:
        return self.__corporation['balance']
    
    @property
    def logo_url(self) -> str:
        return self.__corporation['logoUrl']
    
    @property
    def logo_file_name(self) -> str:
        return self.__corporation['logoFileName']
    
    @property
    def created_date(self) -> datetime:
        datetime_format = get_correct_datetime_format(self.__corporation['createdDate'])
        return datetime.strptime(self.__corporation['createdDate'], datetime_format)
    
    @property
    def modified_date(self) -> datetime:
        datetime_format = get_correct_datetime_format(self.__corporation['modifiedDate'])
        return datetime.strptime(self.__corporation['modifiedDate'], datetime_format)
    
    @property
    def joined_date(self) -> datetime:
        datetime_format = get_correct_datetime_format(self.__payload['joinedDate'])
        return datetime.strptime(self.__payload['joinedDate'], datetime_format)
    
    @property
    def role(self) -> str:
        match self.__payload['role']:
            case 'ADMIN':
                return 'PDG'
            case 'MEMBER':
                return 'Membre'
            
    @property
    def url(self) -> str:
        return f"https://zunivers.zerator.com/corporation/{self.id}"
    
class CorporationBonusAtrb:
    """
    Represents a corporation bonus attributes.
    
    Attributes:
        level (int): The level of the bonus.
    """
    
    def __init__(self, payload: CorporationBonus) -> None:
        self.__payload = payload
    
    @property
    def level(self) -> int:
        return self.__payload['level']

class CorporationBonuses:
    """
    Represents the corporation bonuses.

    Attributes:
        member_count (CorporationBonusAtrb): The member count bonus.
        loot (CorporationBonusAtrb): The loot bonus.
        recycle_lore_dust (CorporationBonusAtrb): The recycle lore dust bonus.
        recycle_lore_fragment (CorporationBonusAtrb): The recycle lore fragment bonus.
    """

    def __init__(self, payload: List[CorporationBonus]) -> None:
        self.__payload = payload

    def __get_bonus_atrb(self, bonus_type: str) -> CorporationBonusAtrb:
        bonus = next((bonus for bonus in self.__payload if bonus['type'] == bonus_type))

        return CorporationBonusAtrb(bonus)

    @property
    def member_count(self) -> CorporationBonusAtrb:
        return self.__get_bonus_atrb('MEMBER_COUNT')
    
    @property
    def loot(self) -> CorporationBonusAtrb:
        return self.__get_bonus_atrb('LOOT')
    
    @property
    def recycle_lore_dust(self) -> CorporationBonusAtrb:
        return self.__get_bonus_atrb('RECYCLE_LORE_DUST')
    
    @property
    def recycle_lore_fragment(self) -> CorporationBonusAtrb:
        return self.__get_bonus_atrb('RECYCLE_LORE_FRAGMENT')

class CorporationDonation:
    """
    Represents a corporation donation.
    
    Attributes:
        amount (int): The amount of the donation.
        date (datetime): The date of the donation.
        user_name (str): The name of the user who made the donation.
        user_id (int): The ID of the user who made the donation.
        user_role (str): The role of the user who made the donation.
    """

    def __init__(self, payload: CorporationLedger) -> None:
        self.__payload = payload

    @property
    def amount(self) -> int:
        return self.__payload['amount']
    
    @property
    def date(self) -> datetime:
        datetime_format = get_correct_datetime_format(self.__payload['date'])

        return datetime.strptime(self.__payload['date'], datetime_format)
    
    @property
    def user_name(self) -> str:
        return self.__payload['user']['discordUserName']
    
    @property
    def user_id(self) -> int:
        return self.__payload['user']['discordId']
    
    @property
    def user_role(self) -> str:
        match self.__payload['role']:
            case 'ADMIN':
                return 'PDG'
            case 'MEMBER':
                return 'Membre'

class CorporationMember:
    """
    Represents a corporation member.
    
    Attributes:
        id (int): The ID of the user.
        name (str): The name of the user.
        role (str): The role of the user.
        joined_date (datetime): The joined date of the user.
        today_donations (int): The amount of donations the user made today.
        total_donations (int): The total amount of donations the user made.
    """

    def __init__(self, payload: CorporationUserAPIResponse) -> None:
        self.__payload = payload

    @property
    def id(self) -> int:
        return self.__payload['user']['discordId']
    
    @property
    def name(self) -> str:
        return self.__payload['user']['discordUserName']
    
    @property
    def role(self) -> str:
        match self.__payload['role']:
            case 'ADMIN':
                return 'PDG'
            case 'MEMBER':
                return 'Membre'
            
    @property
    def joined_date(self) -> datetime:
        datetime_format = get_correct_datetime_format(self.__payload['joinedDate'])

        return datetime.strptime(self.__payload['joinedDate'], datetime_format)

    @property
    def today_donations(self) -> int:
        if 'giveToday' not in self.__payload:
            return 0
        
        return self.__payload['giveToday']

    @property
    def total_donations(self) -> int:
        return self.__payload['giveTotal']

class Corporation:
    """
    Represents a corporation.

    Attributes:
        id (str): The ID of the corporation.
        name (str): The name of the corporation.
        description (str): The description of the corporation.
        balance (int): The balance of the corporation.
        logo_url (str): The URL of the corporation's logo.
        logo_file_name (str): The file name of the corporation's logo.
        created_date (datetime): The created date of the corporation.
        modified_date (datetime): The modified date of the corporation.
        bonuses (CorporationBonuses): The bonuses of the corporation.
        donations (List[CorporationDonation]): The donations made to the corporation.
        members (List[CorporationMember]): The members of the corporation.
        url (str): The URL of the corporation.
    """

    def __init__(self, payload: CorporationAPIResponse) -> None:
        self.__payload = payload

    @property
    def id(self) -> str:
        return self.__payload['id']
    
    @property
    def name(self) -> str:
        return self.__payload['name']
    
    @property
    def description(self) -> str:
        return self.__payload['description']
    
    @property
    def balance(self) -> int:
        return self.__payload['balance']
    
    @property
    def logo_url(self) -> str:
        return self.__payload['logoUrl']
    
    @property
    def logo_file_name(self) -> str:
        return self.__payload['logoFileName']
    
    @property
    def created_date(self) -> datetime:
        datetime_format = get_correct_datetime_format(self.__payload['createdDate'])

        return datetime.strptime(self.__payload['createdDate'], datetime_format)
    
    @property
    def modified_date(self) -> datetime:
        datetime_format = get_correct_datetime_format(self.__payload['modifiedDate'])

        return datetime.strptime(self.__payload['modifiedDate'], datetime_format)
    
    @property
    def bonuses(self) -> CorporationBonuses:
        return CorporationBonuses(self.__payload['corporationBonuses'])
    
    @property
    def donations(self) -> List[CorporationDonation]:
        return [CorporationDonation(donation) for donation in self.__payload['corporationLedgers']]

    @property
    def members(self) -> List[CorporationMember]:
        return [CorporationMember(member) for member in self.__payload['userCorporations']]
    
    @property
    def url(self) -> str:
        return f"https://zunivers.zerator.com/corporation/{self.id}"

    @staticmethod
    def get_all_summary() -> List[CorporationSummary]:
        """
        Retrieve all corporations.

        Returns:
            List[Corporation]: Representing all corporations.
        """
        url = f"{API_BASE_URL}/corporation"
        corporations: List[CorporationSummary] = get_datas(url)

        return corporations

    @staticmethod
    def get_summary_by_id(corporation_id: str) -> CorporationSummary:
        """
        Retrieve a corporation summary by its ID.

        Args:
            corporation_id (str): The ID of the corporation.

        Returns:
            CorporationSummary: Representing the corporation.
        """
        corporations = Corporation.get_all_summary()
        corp = next((corp for corp in corporations if corp['id'] == corporation_id), None)

        if not corp:
            raise ValueError(f"Corporation with ID <{corporation_id}> not found.")

        return corp

    @staticmethod
    def get_summary_by_name(corporation_name: str) -> CorporationSummary:
        """
        Retrieve a corporation summary by its name.

        Args:
            corporation_name (str): The name of the corporation.

        Returns:
            CorporationSummary: Representing the corporation.
        """
        corporations = Corporation.get_all_summary()
        corp = next((corp for corp in corporations if corp['name'] == corporation_name), None)

        if not corp:
            raise ValueError(f"Corporation with name <{corporation_name}> not found.")

        return corp

    @staticmethod
    def get_by_id(corporation_id: str) -> 'Corporation':
        """
        Retrieve a corporation by its ID.

        Args:
            corporation_id (str): The ID of the corporation.

        Returns:
            Corporation: Representing the corporation.
        """
        url = f"{API_BASE_URL}/corporation/{corporation_id}"
        corporation: CorporationAPIResponse = get_datas(url)
        
        if not corporation:
            raise ValueError(f"Corporation with ID <{corporation_id}> not found.")

        return Corporation(corporation)

    @staticmethod
    def get_by_name(corporation_name: str) -> 'Corporation':
        """
        Retrieve a corporation by its name.

        Args:
            corporation_name (str): The name of the corporation.

        Returns:
            Corporation: Representing the corporation.
        """
        corp_summary = Corporation.get_summary_by_name(corporation_name)
        return Corporation.get_by_id(corp_summary['id'])