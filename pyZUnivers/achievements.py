from typing import List, Union
import pytz
from datetime import datetime, timedelta
from .api_responses.achievements import Achievement
from .utils import (
    API_BASE_URL,
    get_datas,
    parse_username
)

CATEGORY_BASE_URL = f"{API_BASE_URL}/achievement"
LOOT_CATEGORY_ID = "8e260bf0-f945-44b2-a9d9-92bf839ee917"
YEARLY_ACHIEVEMENT_ID = "5f2d1288-e3f4-4313-b2ad-d944fbf8e6c7"

class _YearError(Exception):

    def __str__(self) -> str:
        return f'Year number must be between 1 and 3.'

class Achievements:

    def __init__(self, username: str) -> None:
        self.name, self.__parsed_name = parse_username(username)

    def __get_category(self, category_id: str) -> List[Achievement]:
        return get_datas(f"{CATEGORY_BASE_URL}/{self.__parsed_name}/{category_id}")

    def get_yearly(self, year: int) -> Union[bool, '_Date']:
        if 0 > year > 3:
            raise _YearError
        
        category: List[Achievement] = self.__get_category(LOOT_CATEGORY_ID)
        achievement = [x for x in category if x["achievement"]["id"] == YEARLY_ACHIEVEMENT_ID][0]

        progress_items = achievement["progress"]["items"]
        done = 0
        for progress in progress_items:
            if progress["done"]: done += 1
            elif '/365' in progress['name']:
                todo = progress['name']
                todo = todo.replace('◇ ', '')
                current = int(todo.split('/')[0])
                days_todo = 365 - current

        if done >= year:
            return False
        return days_todo