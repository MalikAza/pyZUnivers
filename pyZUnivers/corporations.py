from .api_responses import UserCorporation as UserCorporationAPIResponse

from datetime import datetime
from .utils import (
    get_correct_datetime_format
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