import urllib.parse
from typing import List
from .pins import UserPin
from .utils import (
    get_datas,
    API_BASE_URL
)

class UserOverview:

    def __init__(self, username: str) -> None:
        self.name = username.replace('#0', '') if username.endswith('#0') else username
        self.__parsed_name = urllib.parse.quote(self.name)
        self.__infos = get_datas(f"{API_BASE_URL}/user/{self.__parsed_name}/overview")
        self.__pins = self.__infos['pins']

    @property
    def pins(self) -> List[UserPin]:
        return [UserPin(x) for x in self.__pins]