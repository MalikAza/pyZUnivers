from typing import TypedDict

from .packs import Pack

class Event(TypedDict):
    name: str
    pack: Pack
    balanceCost: None|int
    loreDustCost: None|int
    isOneTime: bool
    beginDate: str
    endDate: str
    isActive: bool