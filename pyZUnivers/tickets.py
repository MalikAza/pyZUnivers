from typing import Literal, TypedDict, List
from .api_responses.tickets import TicketCounts, Ticket, GrattingResult, ExpiredLinkOrNoTicket
from .api_responses.items import InventoryObject
from .utils import (
    get_datas,
    post_datas,
    API_BASE_URL
)

class Result(TypedDict):
    balance: int
    inventories: List[InventoryObject]
    loreDust: int
    loreFragment: int
    luckyLink: List[str]
    userBanner: bool
    nbrTicketScratched: int

class AutoGratting:

    def __init__(self, url: str) -> None:
        self.base_url = f"{API_BASE_URL}/lucky"
        tmp_url = url.split('/')
        self.ticket_code = tmp_url[-1] if len(tmp_url[-1]) else tmp_url[-2]

        self.balance = 0
        self.inventories: List[InventoryObject] = []
        self.loreDust = 0
        self.loreFragment = 0
        self.luckyLink = []
        self.userBanner = False
        self.nbr_ticket_scratched = 0

    def __result(self) -> Result:
        return {
            'balance': self.balance,
            'inventories': self.inventories,
            'loreDust': self.loreDust,
            'loreFragment': self.loreFragment,
            'luckyLink': self.luckyLink,
            'userBanner': self.userBanner,
            'nbrTicketScratched': self.nbr_ticket_scratched
        }

    async def gratting(self, ticket_type: Literal['LR', 'RO', 'ZR'] = 'LR') -> Result|str:
        datas: TicketCounts|ExpiredLinkOrNoTicket = get_datas(f"{self.base_url}/{self.ticket_code}/count")

        if all(key in datas for key in ExpiredLinkOrNoTicket.__annotations__.keys()):
            return datas['message']

        tickets_counters = datas['counts']
        match ticket_type:
            case 'LR':
                count = tickets_counters['LUCKY_RAYOU']
                ticket_type = 'LUCKY_RAYOU'
            case 'RO':
                count = tickets_counters['RAYOU_OFFICIEL']
                ticket_type = 'RAYOU_OFFICIEL'
            case 'ZR':
                count = tickets_counters['ZERA_3000']
                ticket_type = 'ZERA_3000'

        if count == 0: return 'Aucun ticket de ce type trouvé.'

        self.nbr_ticket_scratched = count
        while count > 0:
            ticket: Ticket = get_datas(f"{self.base_url}/{self.ticket_code}?type={ticket_type}")
            ticket_id = ticket['id']

            result: GrattingResult = post_datas(f"{self.base_url}/{ticket_id}")

            if result['balance']:
                self.balance += result['balance']
            if result['loreDust']:
                self.loreDust += result['loreDust']
            if result['loreFragment']:
                self.loreFragment += result['loreFragment']
            elif result['inventories']:
                self.inventories.append(result['inventories'][0])
            elif result['luckyLink'] and result['quantity']:
                count += 1
                self.nbr_ticket_scratched += 1
            elif result['luckyLink']:
                self.luckyLink.append(result['luckyLink'])
            elif result['userBanner']:
                self.userBanner = True

            count -= 1

        return self.__result()