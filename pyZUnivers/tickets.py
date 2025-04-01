from typing import Literal, TypedDict, List
from .api_responses.tickets import TicketCounts, Ticket, GrattingResult, ExpiredLinkOrNoTicket
from .api_responses.items import InventoryObject
from .utils import (
    get_datas,
    post_datas,
    API_BASE_URL
)

class Result(TypedDict):
    """
    Represents the result of a ticket scratching operation.

    Attributes:
        balance (int): The balance after the ticket scratching operation.
        inventories (List[InventoryObject]): The list of inventory objects.
        loreDust (int): The amount of lore dust.
        loreFragment (int): The amount of lore fragments.
        luckyLink (List[str]): The list of lucky links.
        userBanner (bool): Indicates if the user has a banner.
        nbrTicketScratched (int): The number of tickets scratched.
    """
    balance: int
    inventories: List[InventoryObject]
    loreDust: int
    loreFragment: int
    luckyLink: List[str]
    userBanner: bool
    nbrTicketScratched: int

class AutoGratting:
    """
        Initializes a Ticket object.

        Args:
            url (str): The URL of the tickets.
    """

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
        """
        Perform the gratting operation for the specified ticket type.

        Args:
            ticket_type (Literal['LR', 'RO', 'ZR'], optional): The type of ticket to grat. Defaults to 'LR'.

        Returns:
            Union[Result, str]: The result of the gratting operation or an error message.

        Raises:
            None

        """
        datas: TicketCounts|ExpiredLinkOrNoTicket = get_datas(f"{self.base_url}/{self.ticket_code}/count")

        if all(key in datas for key in ExpiredLinkOrNoTicket.__annotations__.keys()):
            return datas['message']

        tickets_counters = datas['counts']
        match ticket_type:
            case 'LR':
                count = tickets_counters['LUCKY_RAYOU']
                ticket_type = 'LUCKY_RAYOU'
            case 'RO':
                count = tickets_counters['RAYOU_OFFICIAL']
                ticket_type = 'RAYOU_OFFICIAL'
            case 'ZR':
                count = tickets_counters['ZERA_3000']
                ticket_type = 'ZERA_3000'

        if count == 0: return 'Aucun ticket de ce type trouvé.'

        self.nbr_ticket_scratched = count
        while count > 0:
            ticket: Ticket = get_datas(f"{self.base_url}/{self.ticket_code}?type={ticket_type}")
            try:
                ticket_id = ticket['id']
            except KeyError:
                self.nbr_ticket_scratched -= count
                count = 0
                continue

            result: GrattingResult = post_datas(f"{self.base_url}/{ticket_id}")

            if 'inventories' in result:
                for item in result['inventories']: self.inventories.append(item)
            if 'luckyLink' in result and 'quantity' in result:
                count += 1
                self.nbr_ticket_scratched += 1
            elif 'luckyLink' in result:
                self.luckyLink.append(result['luckyLink'])
            if 'userBanner' in result:
                self.userBanner = True
            if 'balance' in result:
                self.balance += result['balance']
            if 'loreDust' in result:
                self.loreDust += result['loreDust']
            if 'loreFragment' in result:
                self.loreFragment += result['loreFragment']

            count -= 1

        return self.__result()