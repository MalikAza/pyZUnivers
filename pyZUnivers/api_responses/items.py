from typing import TypedDict, List

from .packs import Pack

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
    score: int
    scoreGolden: int
    isRecyclable: bool
    isTradable: bool
    isCounting: bool
    isCraftable: bool
    isInvocable: bool
    isGoldable: bool
    isUpgradable: bool

class __ItemMoreInfos(TypedDict):
    item: Item
    isGolden: bool
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