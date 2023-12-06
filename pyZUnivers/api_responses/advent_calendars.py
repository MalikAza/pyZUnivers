from typing import TypedDict, List

from items import ItemMetaData

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