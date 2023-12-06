from typing import TypedDict

class ChallengeObject(TypedDict):
    id: str
    description: str
    type: str
    score: int
    rewardLoreDust: int

class ChallengeProgress(TypedDict):
    type: str
    current: int
    max: int
    items: None|str

class Challenges(TypedDict):
    id: str
    beginDate: str
    endDate: str
    challenge: ChallengeObject
    progress: ChallengeProgress
    challengeLog: None|str