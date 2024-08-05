from datetime import datetime
from typing import List

from .errors import UserNotFound
from .api_responses import Challenge as ChallengeType
from .utils import (
    API_BASE_URL,
    ResourceNotFoundError,
    get_correct_datetime_format,
    get_datas,
    parse_username
)

class _ChallengeAtrb:
    """
    A challenge's informations.

    Attributes:
        name (str): The name of the challenge.
        score_gain (int): The score gain of the challenge.
        lore_dust_gain (int): The lore dust gain of the challenge.
        progress (str): The progress of the challenge.
        achieved_date (datetime): The achieved date of the challenge.
    """

    def __init__(self, payload) -> None:
        self.__challenge_item = payload['challenge']
        try:
            achieved = payload['challengeLog']
        except KeyError:
            achieved = None
        try:
            progress = payload['progress']
        except KeyError:
            progress = None

        self.progress = '0/1'
        self.achieved_date = None

        if progress:
            self.progress = f'{progress["current"]}/{progress["max"]}'

        if achieved:
            achieved_date_format = get_correct_datetime_format(achieved['date'])
            self.achieved_date = datetime.strptime(achieved['date'], achieved_date_format)
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
    """
    User's informations about current challenges.

    Attributes:
        name (str): The name of the user.
        first (Challenge): The first challenge.
        second (Challenge): The second challenge.
        third (Challenge): The third challenge.
        begin_date (datetime): The begin date of the challenges.
        end_date (datetime): The end date of the challenges.
    """

    def __init__(self, username : str = None) -> None:
        self.name, self.__parsed_name = parse_username(username) if username else ('', '')
        try:
            self.__infos: List[ChallengeType] = get_datas(f'{API_BASE_URL}/challenge/{self.__parsed_name}')
        except ResourceNotFoundError: raise UserNotFound(self.name)

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
        datetime_format = get_correct_datetime_format(self.__infos[0]['beginDate'])
        return datetime.strptime(self.__infos[0]['beginDate'], datetime_format)
    
    @property
    def end_date(self) -> datetime:
        datetime_format = get_correct_datetime_format(self.__infos[0]['endDate'])
        return datetime.strptime(self.__infos[0]['endDate'], datetime_format)