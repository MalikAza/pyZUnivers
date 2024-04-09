import urllib.parse
from datetime import datetime
from typing import List

from .api_responses import Challenge as ChallengeType
from .utils import (
    API_BASE_URL,
    FULL_DATE_TIME_FORMAT,
    DATE_TIME_FORMAT,
    get_datas
)

class _ChallengeAtrb:

    def __init__(self, payload) -> None:
        self.__challenge_item = payload['challenge']
        achieved = payload['challengeLog']
        progress = payload['progress']

        self.progress = '0/1'
        self.achieved_date = None

        if progress:
            self.progress = f'{progress["current"]}/{progress["max"]}'

        if achieved:
            self.achieved_date = datetime.strptime(achieved['date'], FULL_DATE_TIME_FORMAT)
            self.progress = '✅'

    @property
    def name(self) -> str:
        return self.__challenge_item['description']
    
    @property
    def score_gain(self) -> int:
        return self.__challenge_item['score']
    
    @property
    def lore_dust_gain(self) -> int:
        return self.__challenge_item['rewardLoreDust']

class Challenges:

    def __init__(self, username : str = None) -> None:
        self.name = username.removesuffix('#0')
        self.__parsed_name = urllib.parse.quote(self.name) if username else ""
        self.__infos: List[ChallengeType] = get_datas(f'{API_BASE_URL}/challenge/{self.__parsed_name}')

    @property
    def first(self) -> _ChallengeAtrb:
        return _ChallengeAtrb(self.__infos[0])
    
    @property
    def second(self) -> _ChallengeAtrb:
        return _ChallengeAtrb(self.__infos[1])
    
    @property
    def third(self) -> _ChallengeAtrb:
        return _ChallengeAtrb(self.__infos[2])
    
    @property
    def begin_date(self) -> datetime:
        return datetime.strptime(self.__infos[0]['beginDate'], DATE_TIME_FORMAT)
    
    @property
    def end_date(self) -> datetime:
        return datetime.strptime(self.__infos[0]['endDate'], DATE_TIME_FORMAT)