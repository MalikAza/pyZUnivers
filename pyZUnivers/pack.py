from typing import Union

class Pack:
    """
    Reflects a cards pack.

    Attributes:
        id (str): The id of the pack.
        name (str): The name of the pack.
        year (Union[None, int]): The year of the pack. (4 digits, ex: 2021)
        slug (str): The slug of the pack.
    """

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