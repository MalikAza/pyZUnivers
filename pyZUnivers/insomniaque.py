from typing import List

from .api_responses import Achievement
from .utils import (
    get_datas, 
    API_BASE_URL,
    parse_username
)

class Insomniaque: # TODO: Refacto with achievements.py

    def __init__(self, username: str) -> None:
        _, self.__parsed_name = parse_username(username)
        datas : List[Achievement] = get_datas(f"{API_BASE_URL}/achievement/{self.__parsed_name}/8e260bf0-f945-44b2-a9d9-92bf839ee917")
        self.__datas = datas[2]

    @property
    def name(self) -> str:
        return self.__datas['achievement']['name']
    
    @property
    def description(self) -> str:
        return self.__datas['achievement']['description']
    
    @property
    def reward_score(self) -> int:
        return self.__datas['achievement']['score']
    
    @property
    def done(self) -> bool:
        return bool(self.__datas['id'])
    
    @property
    def progress_done(self) -> bool|list:
        if self.done:
            tmp = []
            for key, value in self.__datas['progress']['items'].items():
                if value:
                    tmp.append(key)
            return tmp
        return False
    
    @property
    def progress_todo(self) -> bool|list:
        if not self.done:
            tmp = []
            for key, value in self.__datas['progress']['items'].items():
                if not value:
                    tmp.append(key)
            return tmp
        return False