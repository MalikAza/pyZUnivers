import unittest
from unittest.mock import patch, MagicMock

from freezegun import freeze_time
import pyZUnivers
from datetime import date, datetime
import pytz

import pyZUnivers.api_responses

class UserLootInfosTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.loot_infos_powaza = pyZUnivers.UserLootInfos('powaza')

    def test_journa(self) -> None:
        self.assertIsInstance(self.loot_infos_powaza.journa, bool)

    def test_bonus(self) -> None:
        self.assertIsInstance(self.loot_infos_powaza.bonus, bool)

    def test_bonus_when(self) -> None:
        self.assertIsInstance(self.loot_infos_powaza.bonus_when, date)

    @freeze_time('2024-04-29')
    def test_bonus_true_missing_journa(self) -> None:
        self.loot_infos_powaza.loot_infos = {
            '2024-04-21': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}, {'type': pyZUnivers.api_responses.LootType.WEEKLY.value}],
            '2024-04-29': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}],
        }

        self.assertTrue(self.loot_infos_powaza.bonus)
        self.assertEqual('2024-05-05', self.loot_infos_powaza.bonus_when.strftime('%Y-%m-%d'))

    @freeze_time('2024-04-29')
    def test_bonus_true_when_journa_not_done_yet(self) -> None:
        self.loot_infos_powaza.loot_infos = {
            '2024-04-22': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}, {'type': pyZUnivers.api_responses.LootType.WEEKLY.value}],
            '2024-04-23': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}],
            '2024-04-24': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}],
            '2024-04-25': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}],
            '2024-04-26': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}],
            '2024-04-27': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}],
            '2024-04-28': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}],
        }

        self.assertTrue(self.loot_infos_powaza.bonus)
        self.assertEqual('2024-04-29', self.loot_infos_powaza.bonus_when.strftime('%Y-%m-%d'))

    @freeze_time('2024-04-29')
    def test_bonus_false_when_journa_is_done(self) -> None:
        self.loot_infos_powaza.loot_infos = {
            '2024-04-22': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}, {'type': pyZUnivers.api_responses.LootType.WEEKLY.value}],
            '2024-04-23': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}],
            '2024-04-24': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}],
            '2024-04-25': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}],
            '2024-04-26': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}],
            '2024-04-27': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}],
            '2024-04-28': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}],
            '2024-04-29': [{'type': pyZUnivers.api_responses.LootType.DAILY.value}],
        }

        self.assertFalse(self.loot_infos_powaza.bonus)
        self.assertEqual('2024-04-29', self.loot_infos_powaza.bonus_when.strftime('%Y-%m-%d'))

    def test_journa_not_done_bonus_needed(self) -> None:
        loot_infos_stub = MagicMock()
        loot_infos_stub.journa = False
        loot_infos_stub.bonus = True
        now = datetime.now(pytz.timezone('Europe/Paris')).strftime('%Y-%m-%d')
        loot_infos_stub.bonus_when.strftime.return_value = now

        with (
            patch('pyZUnivers.user.UserLootInfos', return_value=loot_infos_stub),
            patch('pyZUnivers.user.is_advent_calendar', return_value=False)
            ):
            result = pyZUnivers.User.get_checker('powaza')

        self.assertEqual(result, {'journa': False, 'bonus': False, 'advent': None})