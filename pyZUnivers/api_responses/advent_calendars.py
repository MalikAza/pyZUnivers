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

class ItemMetaData(TypedDict):
    item: Item
    isGolden: bool
    upgradeLevel: int

class Calendar(TypedDict):
    index: int
    openedDate: None|str
    openableDate: str
    itemMetadata: None|ItemMetaData
    banner: None
    loreDust: int
    loreFragment: int
    balance: int
    luckyType: str
    isOpenable: bool

class AdventCalendar(TypedDict):
    initDate: str
    beginDate: str
    endDate: str
    calendars: List[Calendar]