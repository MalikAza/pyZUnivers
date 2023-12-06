from typing import TypedDict, List

class Loot(TypedDict):
    date: str
    count: int

class LootInfos(TypedDict):
    lootInfos: List[Loot]