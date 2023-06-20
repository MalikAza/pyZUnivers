class _LeaderBoardData:

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

    def __init__(self, payload) -> None:
        self.position = payload['position']
        self.score = payload['score']
        if payload['data']:
            self.data = _LeaderBoardData(payload['data'])

class UserLeaderboards:

    def __init__(self, payload) -> None:
        self.__payload = payload
        for leaderboard in self.__payload:
            setattr(self, f'__{leaderboard["type"]}', leaderboard)

    @property
    def globals(self):
        return _LeaderBoard(getattr(self, '__GLOBAL'))
    
    @property
    def tradeless(self):
        tradeless = getattr(self, '__TRADELESS')

        if not tradeless: return False
        return _LeaderBoard(tradeless)
    
    @property
    def inventory_unique(self):
        return _LeaderBoard(getattr(self, '__INVENTORY_UNIQUE'))
    
    @property
    def inventory_unique_normal(self):
        return _LeaderBoard(getattr(self, '__INVENTORY_UNIQUE_NORMAL'))
    
    @property
    def challenge(self):
        return _LeaderBoard(getattr(self, '__CHALLENGE'))
    
    @property
    def inventory_unique_golden(self):
        return _LeaderBoard(getattr(self, '__INVENTORY_UNIQUE_GOLDEN'))
    
    @property
    def inventory(self):
        return _LeaderBoard(getattr(self, '__INVENTORY'))
    
    @property
    def constellations(self):
        constellation = getattr(self, '__UPGRADE')

        if not constellation: return False
        return _LeaderBoard(constellation)
    
    @property
    def achievement(self):
        return _LeaderBoard(getattr(self, '__ACHIEVEMENT'))
    
    @property
    def reputation(self):
        return _LeaderBoard(getattr(self, '__REPUTATION'))