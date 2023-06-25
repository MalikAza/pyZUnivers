from .user import User
from .overview import UserOverview
from .loot_infos import UserLootInfos

def get_user_overview(username: str) -> UserOverview:
    return UserOverview(username)

def get_user_loot_infos(username: str) -> UserLootInfos:
    return UserLootInfos(username)