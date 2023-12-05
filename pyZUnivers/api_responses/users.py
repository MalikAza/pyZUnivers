from typing import TypedDict, List

class User(TypedDict):
    id: str
    discordId: None|int
    discordUserName: str
    discordGlobalName: None|str
    discordAvatar: None|str
    balance: None|int
    loreDust: None|int
    loreFragment: None|int
    upgradeDust: None|int
    rank: None|int
    userBanner: None|str
    isActive: bool
    createdDate: None|str

class AscensionUser(TypedDict):
    user: User
    maxFloorIndex: int
    towerLogCount: int
    towerLogCountByFloor: List[int]