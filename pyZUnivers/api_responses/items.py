from typing import TypedDict, List

from .packs import Pack

ShinyLevels = TypedDict("ShinyLevels", {0: bool, 1: bool, 2: bool})
ShinyScores = TypedDict("ShinyScores", {0: int, 1: int, 2: int})

class Item(TypedDict):
    id: str
    name: str
    slug: str
    genre: str
    rarity: int
    identifier: int
    description: None|str
    reference: None|str
    pack: Pack
    urls: List[str]
    scores: ShinyScores
    shinyLevels: ShinyLevels
    isRecyclable: bool
    isTradable: bool
    isCounting: bool
    isCraftable: bool
    isInvocable: bool
    isGoldable: bool
    isUpgradable: bool

class __ItemMoreInfos(TypedDict):
    item: Item
    shinyLevel: int
    upgradeLevel: int

class ItemMetaData(__ItemMoreInfos):
    pass

class InventoryObject(__ItemMoreInfos):
    id: str
    quantity: int

class Inventory(TypedDict):
    inventory: InventoryObject
    date: str

class BestInventoryLog(__ItemMoreInfos):
    date: str
    isPity: bool
    source: str
    deltaQuantity: int

class UserInventoryObject(InventoryObject):
    isFusion: bool
    isFusionComponent: bool