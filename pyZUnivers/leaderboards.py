from typing import Union

class _LeaderBoardData:
    """
    Data of the user in the leaderboard.

    Attributes:
        total (int): The total of cards the user have for this leaderboard.
        total_distinct (int): The total of distinct cards the user have for this leaderboard.
        maxed (int): The total of maxed upgraded cards the user have for this leaderboard.
        achievement_count (int): The achievement count of the user in the leaderboard.
    """

    def __init__(self, datas) -> None:
        for key in datas: # Can't unpack, so don't change this logic
            match key:
                case 'total':
                    self.total = datas[key]
                    break
                case 'totalDistinct':
                    self.total_distinct = datas[key]
                    break
                case 'maxed':
                    self.maxed = datas[key]
                    break
                case 'achievementCount':
                    self.achievement_count = datas[key]

class _LeaderBoard:
    """
    Reflects a leaderboard.

    Attributes:
        position (int): The position of the user in the leaderboard.
        score (int): The score of the user in the leaderboard.
        data (_LeaderBoardData): The data of the user in the leaderboard.
    """

    def __init__(self, payload) -> None:
        self.position = payload['position']
        self.score = payload['score']
        if 'data' in payload:
            self.data = _LeaderBoardData(payload['data'])

class UserLeaderboards:
    """
    Differents leaderboards of a user.

    Attributes:
        globals (_LeaderBoard): The global leaderboard of the user.
        tradeless (Union[bool, _LeaderBoard]): The tradeless leaderboard of the user.
        inventory_unique (_LeaderBoard): The inventory unique leaderboard of the user.
        inventory_unique_normal (_LeaderBoard): The inventory unique normal leaderboard of the user.
        challenge (_LeaderBoard): The challenge leaderboard of the user.
        inventory_unique_golden (_LeaderBoard): The inventory unique golden leaderboard of the user.
        inventory (_LeaderBoard): The inventory leaderboard of the user.
        constellations (Union[bool, _LeaderBoard]): The constellations leaderboard of the user.
        achievement (_LeaderBoard): The achievement leaderboard of the user.
        reputation (_LeaderBoard): The reputation leaderboard of the user.
    """

    def __init__(self, payload) -> None:
        self.__payload = payload
        for leaderboard in self.__payload:
            setattr(self, f'__{leaderboard["type"]}', leaderboard)

    @property
    def globals(self) -> _LeaderBoard:
        return _LeaderBoard(getattr(self, '__GLOBAL'))
    
    @property
    def tradeless(self) -> Union[bool, _LeaderBoard]:
        try:
            tradeless = getattr(self, '__TRADELESS')
            return _LeaderBoard(tradeless)
        except AttributeError:
            return False
    
    @property
    def inventory_unique(self) -> _LeaderBoard:
        return _LeaderBoard(getattr(self, '__INVENTORY_UNIQUE'))
    
    @property
    def inventory_unique_normal(self) -> _LeaderBoard:
        return _LeaderBoard(getattr(self, '__INVENTORY_UNIQUE_NORMAL'))
    
    @property
    def challenge(self) -> _LeaderBoard:
        return _LeaderBoard(getattr(self, '__CHALLENGE'))
    
    @property
    def inventory_unique_golden(self) -> _LeaderBoard:
        return _LeaderBoard(getattr(self, '__INVENTORY_UNIQUE_GOLDEN'))
    
    @property
    def constellations(self) -> Union[bool, _LeaderBoard]:
        try:
            constellation = getattr(self, '__UPGRADE')
            return _LeaderBoard(constellation)
        except AttributeError:
            return False
    
    @property
    def achievement(self) -> _LeaderBoard:
        return _LeaderBoard(getattr(self, '__ACHIEVEMENT'))
    
    @property
    def reputation(self) -> _LeaderBoard:
        return _LeaderBoard(getattr(self, '__REPUTATION'))