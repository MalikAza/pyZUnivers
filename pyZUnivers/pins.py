from .pack import Pack
from typing import Union, List

class UserPin:

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