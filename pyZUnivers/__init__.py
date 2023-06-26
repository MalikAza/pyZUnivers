from .user import User
from .overview import UserOverview
from .loot_infos import UserLootInfos
from .challenges import Challenges
from .reputation import UserReputation

def get_user_overview(username: str) -> UserOverview:
    return UserOverview(username)

def get_user_loot_infos(username: str) -> UserLootInfos:
    return UserLootInfos(username)

def get_challenges(username: str = None) -> Challenges:
    return Challenges(username)

def get_user_reputations(username: str) -> UserReputation:
    return UserReputation(username)