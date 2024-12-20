from typing import TypedDict, List

from .items import Inventory, BestInventoryLog
from .towers import TowerStat, Reputation

class Rank(TypedDict):
    id: str
    name: str

class BannerObject(TypedDict):
    id: str
    title: str
    name: str
    imageUrl: str

class Banner(TypedDict):
    id: str
    date: str
    banner: BannerObject

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
    rank: None|Rank
    userBanner: None|Banner
    isActive: bool
    createdDate: None|str

class AscensionUser(TypedDict):
    user: User
    maxFloorIndex: int
    towerLogCount: int
    towerLogCountByFloor: List[int]

class CountByRarity(TypedDict):
    rarity: int
    shinyLevel: int
    upgradeLevel: int
    inventoryCount: int
    inventoryUniqueCount: int
    itemCount: int
    upgradableItemCount: int
    chromaItemCount: int

class Overview(TypedDict):
    countByRarity: List[CountByRarity]
    pins: List[Inventory]
    bestInventoryLogs: List[BestInventoryLog]
    invokeBeforePity: int
    towerStat: TowerStat

class Tower(TypedDict):
    towerStats: List[TowerStat]
    reputations: List[Reputation]

class Subscription:
    beginDate: str
    endDate: str

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

class Base(TypedDict):
    user: User
    leaderboards: List[LeaderboardObject]
    inventoryCount: int
    inventoryUniqueCount: int
    inventoryUniqueGoldenCount: int
    inventoryUniqueUpgradableCount: int
    inventoryUniqueGoldenUpgradableCount: int
    itemCount: int
    upgradableItemCount: int
    luckyCount: int
    achievementLogCount: int
    achievementCount: int
    subscription: Subscription
    tradeCount: int
    tradeCountToday: int
    tradeLimit: int
    subscriptionBonusCount: int
    subscriptionBonusLimit: int