from .api_responses import Ascension as AscensionType
from .api_responses.items import UserInventoryObject

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

JOURNA_BONUS_TICKET_CHANNEL_ID = 808432657838768168
INVOCATION_IM_FUSION_CHANNEL_ID = 808432737697661008
PROFIL_SUCCES_DEFIS_CHANNEL_ID = 785944890453393408
FORGE_CHANNEL_ID = 813980453924896778
VORTEX_CHANNEL_ID = 824253593892290561
ON_PARLE_DE_ZUNIVERS_CHANNEL_ID = 785965752628543558

class Checker(TypedDict):
    """
    Represents a checker object with boolean properties.

    Attributes:
        journa (bool): Indicates if the journa property is True or False.
        bonus (bool): Indicates if the bonus property is True or False.
        advent (bool): Indicates if the advent property is True or False.
    """
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
    """
    Fetches data from the specified URL and returns it as a list or dictionary.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        Union[List, Dict]: The fetched data as a list or dictionary.

    Raises:
        ZUniversAPIError: If there is an error decoding the JSON response.

    """
    with requests.get(url) as resp:
        try:
            datas = resp.json()
        except Exception as e:
            if type(e).__name__ == 'JSONDecodeError': raise ZUniversAPIError(url)
            else: raise e

    return datas

def post_datas(url) -> List | Dict:
    """
    Sends a POST request to the specified URL and returns the response data.

    Args:
        url (str): The URL to send the POST request to.

    Returns:
        Union[List, Dict]: The response data as a list or dictionary.

    Raises:
        ZUniversAPIError: If there is an error decoding the response data as JSON.
        Exception: If there is any other exception during the request.

    """
    with requests.post(url) as resp:
        try:
            datas = resp.json()
        except Exception as e:
            if type(e).__name__ == 'JSONDecodeError': raise ZUniversAPIError(url)
            else: raise e

    return datas

def parse_username(username: str) -> tuple[str, str]:
    """
    Parses the given username and returns a tuple containing the original username and the parsed name.

    Args:
        username (str): The username to be parsed.

    Returns:
        tuple[str, str]: A tuple containing the original username and the parsed name.
    """
    if username: username.removesuffix('#0')
    parsed_name = urllib.parse.quote(username) if username else ""

    return (username, parsed_name)

def is_advent_calendar() -> bool:
    """
    Check if the current date is within the Advent calendar period.

    Returns:
        bool: True if the current date is between December 1st and December 25th (inclusive), False otherwise.
    """
    day, month = [int(x) for x in datetime.now(pytz.timezone('Europe/Paris')).strftime("%d-%m").split("-")]
    if month == 12 and 1 <= day <= 25: return True
    return False

def get_ascension_leaderboard(*usernames: str):
    """
    Retrieves the ascension leaderboard for the given usernames.

    Args:
        *usernames (str): Variable number of usernames to retrieve the leaderboard for.

    Returns:
        list: A sorted list of users in the ascension leaderboard, sorted by maxFloorIndex and towerLogCount.
    """
    if len(usernames) == 1 and isinstance(usernames[0], list): usernames = usernames[0]
    usernames = ['&discordUserName=' + parse_username(username)[-1] for username in usernames]
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

def get_inventory(username: str, search: str = None) -> List[UserInventoryObject]:
    """
    Retrieve the inventory of a user.

    Args:
        username (str): The username of the user.
        search (str, optional): The search query to filter the inventory. Defaults to None.

    Returns:
        List[UserInventoryObject]: A list of UserInventoryObject representing the user's inventory.
    """
    base_url = f"{API_BASE_URL}/inventory/{parse_username(username)[-1]}"
    if search: base_url += f'?search={search}'

    result: List[UserInventoryObject] = get_datas(base_url)

    return result

def best_inventory(username: str, limit: int = 10) -> List[UserInventoryObject]:
    """
    Retrieves the best inventory items for a given username.

    Args:
        username (str): The username for which to retrieve the inventory.
        limit (int, optional): The maximum number of items to return. Defaults to 10.

    Returns:
        List[UserInventoryObject]: A list of the best inventory items, sorted by score.

    """
    inventory = get_inventory(username)

    def sorted_callback(x: UserInventoryObject) -> int:
        if x["isGolden"]: return x["item"]["scoreGolden"]
        return x["item"]["score"]
    
    inventory = sorted(inventory, key=sorted_callback, reverse=True)

    return inventory[:limit]

def get_correct_datetime_format(date: str) -> str:
    """
    Checks if the given date string is in the format %Y-%m-%dT%H:%M:%S.%f or %Y-%m-%dT%H:%M:%S.
    
    Parameters:
        date (str): The date string to be checked.
        
    Returns:
        str: The appropriate datetime format string based on the presence of milliseconds.
    """
    return FULL_DATE_TIME_FORMAT if "." in date else DATE_TIME_FORMAT