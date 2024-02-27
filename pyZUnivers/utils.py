from .api_responses import Ascension as AscensionType

import requests
from typing import List, Dict, TypedDict
from datetime import datetime
import pytz
import urllib.parse

API_BASE_URL = "https://zunivers-api.zerator.com/public"
PLAYER_BASE_URL = "https://zunivers.zerator.com/joueur"
DATE_FORMAT = '%Y-%m-%d'
DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
FULL_DATE_TIME_FORMAT = f"{DATE_TIME_FORMAT}.%f"
DISCORD_DATE_FORMAT = "%d/%m/%Y %H:%M"

ADVENT_INDEX = {
    "1*": 1,
    "2*": 2,
    "ticket": 3,
    "dust": 4,
    "fragment": 5,
    "balance": 6,
    "1*+": 7,
    "3*": 8,
    "banner": 9,
    "2*+": 10,
    "3*+": 11,
    "4*": 12,
    "4*+": 13
}
class Checker(TypedDict):
    journa: bool
    bonus: bool
    advent: bool

class ZUniversAPIError(Exception):
    def __init__(self, url) -> None:
        self.url = url
        self.message = 'Something went wrong on ZUnivers API.'

    def __str__(self) -> str:
        return f'{self.message} EndPoint: {self.url}'

def get_datas(url) -> List | Dict:
    with requests.get(url) as resp:
        try:
            datas = resp.json()
        except Exception as e:
            if type(e).__name__ == 'JSONDecodeError': raise ZUniversAPIError(url)
            else: raise e

    return datas

def parse_username(username: str) -> tuple[str, str]:
    username.removesuffix('#0')
    parsed_name = urllib.parse.quote(username) if username else ""

    return (username, parsed_name)

def is_advent_calendar() -> bool:
    day, month = [int(x) for x in datetime.now(pytz.timezone('Europe/Paris')).strftime("%d-%m").split("-")]
    if month == 12 and 1 <= day <= 25: return True
    return False

def get_ascension_leaderboard(*usernames: str):
    if len(usernames) == 1 and isinstance(usernames[0], list): usernames = usernames[0]
    usernames = list(map(lambda x: '&discordUserName=' + urllib.parse.quote(x.removesuffix('#0')), usernames))
    url = f"{API_BASE_URL}/tower/leaderboard?seasonOffset=0"
    for username in usernames: url += username

    datas: AscensionType = get_datas(url)
    users = datas["users"]
    for user in users:
        if not user["maxFloorIndex"]: user['maxFloorIndex'] = 0
        user["maxFloorIndex"] += 1

    return sorted(
        users,
        key=lambda x: (x["maxFloorIndex"], -x["towerLogCount"]),
        reverse=True
    )