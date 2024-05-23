from .api_responses import Tower
from .utils import (
    API_BASE_URL,
    get_datas,
    parse_username
)

class _ReputationClan:
    """
    Represents a clan of a user's reputation.

    Attributes:
        name (str): The name of the clan.
        level_name (str): The user's reputation level name in the clan.
        progress (str): The user's progress in the clan. (e.g. "100/100")
    """

    def __init__(self, payload) -> None:
        self.__payload = payload
        self.__reputation_level = payload['reputationLevel']

    @property
    def name(self) -> str:
        return self.__payload['reputation']['name']
    
    @property
    def level_name(self) -> str:
        return self.__reputation_level['name']
    
    @property
    def progress(self) -> str:
        return f"{self.__payload['value']}/{self.__reputation_level['toValue'] + 1}"

class UserReputation:
    """
    Represents the reputation of a user.

    Attributes:
        name (str): The name of the user.
        first (_ReputationClan): The first clan of the user.
        second (_ReputationClan): The second clan of the user.
        third (_ReputationClan): The third clan of the user.
        fourth (_ReputationClan): The fourth clan of the user.
        fifth (_ReputationClan): The fifth clan of the user.
    """

    def __init__(self, username: str) -> None:
        self.name, self.__parsed_name = parse_username(username)
        datas: Tower = get_datas(f"{API_BASE_URL}/tower/{self.__parsed_name}")
        self.__infos = datas['reputations']

    @property
    def first(self) -> _ReputationClan:
        return _ReputationClan(self.__infos[0])
    
    @property
    def second(self) -> _ReputationClan:
        return _ReputationClan(self.__infos[1])
    
    @property
    def third(self) -> _ReputationClan:
        return _ReputationClan(self.__infos[2])
    
    @property
    def fourth(self) -> _ReputationClan:
        return _ReputationClan(self.__infos[3])
    
    @property
    def fifth(self) -> _ReputationClan:
        return _ReputationClan(self.__infos[4])