from datetime import datetime

from .api_responses import Season
from .utils import (
    get_datas,
    API_BASE_URL,
    DATE_FORMAT
)

class _FloorIndexError(Exception):

    def __str__(self) -> str:
        return f'Floor number must be between 1 and 6.'

class _FloorsDropRates:
    """
    Represents the drop rates for different rarities in a floor.

    Attributes:
        rarity_one_normal (str): Returns the drop rate for rarity one normal cards.
        rarity_two_normal (str): Returns the drop rate for rarity two normal cards.
        rarity_three_normal (str): Returns the drop rate for rarity three normal cards.
        rarity_four_normal (str): Returns the drop rate for rarity four normal cards.
        rarity_one_golden (str): Returns the drop rate for rarity one golden cards.
        rarity_two_golden (str): Returns the drop rate for rarity two golden cards.
        rarity_three_golden (str): Returns the drop rate for rarity three golden cards.
        rarity_four_golden (str): Returns the drop rate for rarity four golden cards.
    """

    def __init__(self, payload) -> None:
        self.__drop_rates = payload['dropRates']

    @property
    def rarity_one_normal(self) -> str:
        return f"{self.__drop_rates[0]['rate']}%"
    
    @property
    def rarity_two_normal(self) -> str:
        return f"{self.__drop_rates[1]['rate']}%"
    
    @property
    def rarity_three_normal(self) -> str:
        return f"{self.__drop_rates[2]['rate']}%"
    
    @property
    def rarity_four_normal(self) -> str:
        return f"{self.__drop_rates[3]['rate']}%"
    
    @property
    def rarity_one_golden(self) -> str:
        return f"{self.__drop_rates[4]['rate']}%"
    
    @property
    def rarity_two_golden(self) -> str:
        return f"{self.__drop_rates[5]['rate']}%"
    
    @property
    def rarity_three_golden(self) -> str:
        return f"{self.__drop_rates[6]['rate']}%"
    
    @property
    def rarity_four_golden(self) -> str:
        return f"{self.__drop_rates[7]['rate']}%"
    

class Vortex:
    """
    Represents a Vortex in the game.

    Attributes:
        name (str): Returns the name of the vortex.
        pack_name (str): Returns the name of the pack associated with the vortex.
        pack_year (int): Returns the year of the pack associated with the vortex.
        reputation_name (str): Returns the name of the reputation associated with the vortex.
        begin_date (datetime): Returns the begin date of the vortex season.
        end_date (datetime): Returns the end date of the vortex season.

    Methods:
        get_floor_drop_rates(floor_number: int) -> _FloorsDropRates:
            Returns the drop rates for a specific floor in the vortex tower.

    """

    def __init__(self) -> None:
        self.__season: Season = get_datas(f'{API_BASE_URL}/tower/season')
        self.__tower = self.__season['tower']

    @property
    def name(self) -> str:
        return self.__tower['name']
    
    @property
    def pack_name(self) -> str:
        return self.__tower['pack']['name']
    
    @property
    def pack_year(self) -> int:
        return self.__tower['pack']['year']

    @property
    def reputation_name(self) -> str:
        return self.__tower['reputation']['name']
    
    @property
    def begin_date(self) -> datetime:
        return datetime.strptime(self.__season['beginDate'], DATE_FORMAT)
    
    @property
    def end_date(self) -> datetime:
        return datetime.strptime(self.__season['endDate'], DATE_FORMAT)
    
    def get_floor_drop_rates(self, floor_number : int) -> _FloorsDropRates:
        """
        Returns the drop rates for a specific floor in the vortex tower.

        Args:
            floor_number (int): The number of the floor (1-5).

        Returns:
            _FloorsDropRates: The drop rates for the specified floor.

        Raises:
            _FloorIndexError: If the floor number is invalid.
        """
        floor_number = abs(floor_number-1)

        if floor_number > 5: raise _FloorIndexError

        return _FloorsDropRates(self.__tower['towerFloors'][floor_number])