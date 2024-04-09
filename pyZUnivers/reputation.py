import urllib.parse

from .api_responses import Tower
from .utils import (
    API_BASE_URL,
    get_datas
)

class _ReputationClan:

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

    def __init__(self, username: str) -> None:
        self.name = username.removesuffix('#0')
        self.__parsed_name = urllib.parse.quote(self.name)
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