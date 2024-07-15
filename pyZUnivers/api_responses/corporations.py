from typing import List, TypedDict

class BaseCorporation(TypedDict):
    id: str
    name: str
    description: str
    balance: int
    logoUrl: str
    createdDate: str
    modifiedDate: str

class UserCorporationSummary(BaseCorporation):
    logoFileName: str

class UserCorporation(TypedDict):
    corporation: UserCorporationSummary
    joinedDate: str
    role: str

class CorporationSummary(BaseCorporation):
    currentBonusLevel: int
    totalBonusLevel: int
    currentMemberCount: int
    totalMemberCount: int

class CorporationBonus(TypedDict):
    type: str
    level: int

class CorporationUserMoreInfos(TypedDict):
    discordAvatar: str
    discordId: str
    discordUserName: str
    discordGlobalName: str
    isActive: bool

class BaseCorporationPlayer(TypedDict):
    role: str
    user: CorporationUserMoreInfos

class CorporationLedger(BaseCorporationPlayer):
    amount: int
    date: str

class CorporationUser(BaseCorporationPlayer):
    giveToday: int
    giveTotal: int
    joinedDate: str

class Corporation(UserCorporationSummary):
    corporationBonuses: List[CorporationBonus]
    corporationLedgers: List[CorporationLedger]
    userCorporations: List[CorporationUser]