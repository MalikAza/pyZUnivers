from typing import TypedDict, List

from .items import Item
from .packs import Pack

class TowerStat(TypedDict):
    maxFloorIndex: int
    towerLogCount: int
    towerSeasonIndex: int
    isCurrentTowerSeason: None|bool
    towerSeasonBeginDate: str
    towerSeasonEndDate: str
    towerName: str
    items: List[Item]
    roundCount: None|int
    maxRoundIndex: None|int

class ReputationObject(TypedDict):
    id: str
    name: str

class ReputationLevel(TypedDict):
    id: str
    index: int
    name: str
    fromValue: int
    toValue: int

class Reputation(TypedDict):
    id: str
    reputation: ReputationObject
    value: int
    reputationLevel: ReputationLevel

class DropRate(TypedDict):
    id: str
    rarity: int
    shinyLevel: bool
    rate: int

class TowerFloor(TypedDict):
    id: str
    index: int
    rate: int
    dropRates: List[DropRate]

class Tower(TypedDict):
    id: str
    index: int
    name: str
    imageUrl: str
    pack: Pack
    reputation: ReputationObject
    towerFloors: List[TowerFloor]

class Season(TypedDict):
    id: str
    index: int
    tower: Tower
    beginDate: str
    endDate: str