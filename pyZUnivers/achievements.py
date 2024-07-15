from typing import List
from .api_responses.achievements import Achievement
from .utils import (
    API_BASE_URL,
    get_datas,
    parse_username
)

CATEGORY_BASE_URL = f"{API_BASE_URL}/achievement"
LOOT_CATEGORY_ID = "8e260bf0-f945-44b2-a9d9-92bf839ee917"
YEARLY_ACHIEVEMENT_IDS = [
    'a43f9fdc-1b05-402e-aae1-8d4fa0592327',
    '60c91e97-df2f-420d-a5db-1225e6f73703',
    '5f2d1288-e3f4-4313-b2ad-d944fbf8e6c7'
]

class _YearError(Exception):

    def __str__(self) -> str:
        return f'Year number must be between 1 and 3.'

class Achievements:
    """
    User achievements.

    Attributes:
        name (str): The name of the user.
    """

    def __init__(self, username: str) -> None:
        self.name, self.__parsed_name = parse_username(username)

    def __get_category(self, category_id: str) -> List[Achievement]:
        return get_datas(f"{CATEGORY_BASE_URL}/{self.__parsed_name}/{category_id}")

    def get_yearly(self, year: int) -> bool|int:
        """
        Get the number of days left to complete the yearly achievement for the given year.

        Args:
            year (int): How many year(s) for the achievement.

        Returns:
            bool|int: The number of days left to complete the yearly achievement. Returns False if the achievement is not unlocked.

        Raises:
            _YearError: If the year is not within the valid range (1-3).

        """
        if 0 > year > 3:
            raise _YearError()
        
        category: List[Achievement] = self.__get_category(LOOT_CATEGORY_ID)
        achievement = [x for x in category if x["achievement"]["id"] == YEARLY_ACHIEVEMENT_IDS[year-1]][0]

        # achievement unlocked
        progress = achievement['progress'] if 'progress' in achievement else None
        if not progress: return False

        # achievement locked
        progress_items = achievement["progress"]["items"]

        undone = 0
        for item in progress_items:
            if not item['done']: undone += 1
            if '/365' in item['name']:
                current = int(item['name'].replace('◇ ', '').split('/')[0])

        days_todo = 365 - current + (365*(undone-1))

        return days_todo