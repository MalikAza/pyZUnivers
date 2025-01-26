from enum import Enum
from typing import Dict, TypedDict, List

class LootType(Enum):
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'

class Loot(TypedDict):
    amount: int
    baseAmount: int
    corporationAmount: int
    subscriptionAmount: int
    corporationBonusLevel: int
    type: LootType
    date: str

LootInfos = Dict[str, List[Loot]]