from typing import TypedDict, List

from .users import AscensionUser

class Ascension(TypedDict):
    users: List[AscensionUser]