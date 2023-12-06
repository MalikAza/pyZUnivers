from typing import TypedDict, List

from .users import AscensionUser

class Ascension(TypedDict):
    users: List[AscensionUser]

class DataTotal(TypedDict):
    total: int

class DataUpgrade(DataTotal):
    maxed: int

class DataAchievement(TypedDict):
    achievementCount: int

class DataInventory(DataTotal):
    totalDistinct: int

class LeaderboardObject(TypedDict):
    position: int
    score: int
    type: str
    data: None|DataInventory|DataTotal|DataAchievement|DataUpgrade