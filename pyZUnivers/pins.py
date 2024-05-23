from .pack import Pack
from typing import Union, List

class UserPin:
    """
    Represents a user card that has been pinned.

    Attributes:
        id (str): The id of the pin.
        name (str): The name of the pin.
        type (str): The type of the pin.
        rarity (int): The rarity of the pin.
        identifier (int): The identifier of the pin.
        description (str): The description of the pin.
        reference (str): The reference of the pin.
        pack (Pack): The pack of the pin.
        image_urls (List[str]): The image urls of the pin.
        score (int): The score of the pin.
        score_golden (int): The score of the golden pin.
        is_recyclable (bool): Whether the pin is recyclable.
        is_tradable (bool): Whether the pin is tradable.
        is_counting (bool): Whether the pin is counting.
        is_craftable (bool): Whether the pin is craftable.
        is_invocable (bool): Whether the pin is invocable.
        is_goldable (bool): Whether the pin is goldable.
        is_upgradable (bool): Whether the pin is upgradable.
        is_golden (bool): Whether the pin is golden.
    """
    
    def __init__(self, payload) -> None:
        self.__payload = payload['inventory']
        self.__item = self.__payload['item']

    @property
    def id(self) -> str:
        return self.__item['id']
    
    @property
    def name(self) -> str:
        return self.__item['name']
    
    @property
    def type(self) -> str:
        return self.__item['genre']
    
    @property
    def rarity(self) -> int:
        return self.__item['rarity']
    
    @property
    def identifier(self) -> int:
        return self.__item['identifier']
    
    @property
    def description(self) -> Union[str, None]:
        return self.__item['description']
    
    @property
    def reference(self) -> Union[str, None]:
        return self.__item['reference']
    
    @property
    def pack(self) -> Pack:
        return Pack(self.__item['pack'])
    
    @property
    def image_urls(self) -> List[str]:
        return [x for x in self.__item['urls']]
    
    @property
    def score(self) -> int:
        return self.__item['score']
    
    @property
    def score_golden(self) -> int:
        return self.__item['scoreGolden']
    
    @property
    def is_recyclable(self) -> bool:
        return self.__item['isRecyclable']
    
    @property
    def is_tradable(self) -> bool:
        return self.__item['isTradable']
    
    @property
    def is_counting(self) -> bool:
        return self.__item['isCounting']
    
    @property
    def is_craftable(self) -> bool:
        return self.__item['isCraftable']
    
    @property
    def is_invocable(self) -> bool:
        return self.__item['isInvocable']
    
    @property
    def is_goldable(self) -> bool:
        return self.__item['isGoldable']
    
    @property
    def is_upgradable(self) -> bool:
        return self.__item['isUpgradable']
    
    @property
    def is_golden(self) -> bool:
        return self.__payload['isGolden']