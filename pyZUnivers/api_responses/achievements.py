from typing import TypedDict, List

class ItemProgress(TypedDict):
    name: str
    done: bool

class Progress(TypedDict):
    type: str
    current: int
    max: int
    items: None|List[ItemProgress]

class AchievementObject(TypedDict):
    id: str
    name: str
    slug: str
    description: str
    featOfStrength: bool
    isDeletable: bool
    score: int
    rewardLoreDust: None|int
    rewardBanner: None|int
    rewardItem: None|int

class Achievement(TypedDict):
    id: None|str
    achievement: AchievementObject
    date: None|str
    deleteDate: None|str
    progress: Progress