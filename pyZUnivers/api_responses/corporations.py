from typing import TypedDict

class UserCorporationSummary(TypedDict):
    id: str
    name: str
    description: str
    balance: int
    logoUrl: str
    logoFileName: str
    createdDate: str
    modifiedDate: str

class UserCorporation(TypedDict):
    corporation: UserCorporationSummary
    joinedDate: str
    role: str