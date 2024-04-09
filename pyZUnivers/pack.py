from typing import Union

class Pack:

    def __init__(self, payload) -> None:
        self.__payload = payload

    @property
    def id(self) -> str:
        return self.__payload['id']
    
    @property
    def name(self) -> str:
        return self.__payload['name']
    
    @property
    def year(self) -> Union[None, int]:
        if not self.__payload['year']: return None
        return self.__payload['year']
    
    @property
    def slug(self) -> str:
        return self.__payload['slug']