from .items import InventoryObject
from typing import TypedDict, List

class TicketCountsObject(TypedDict):
    ZERA_3000: int
    LUCKY_RAYOU: int
    RAYOU_OFFICIEL: int

class TicketCounts(TypedDict):
    counts: TicketCountsObject

class Ticket(TypedDict):
    id: str
    type: str
    value: int

class GrattingResult(TypedDict):
    balance: int|None
    inventories: List[InventoryObject]|None
    loreDust: int|None
    loreFragment: int|None
    luckyLink: str|None
    quantity: int|None
    ticketId: str|None
    userBanner: str|None