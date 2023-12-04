import unittest
import pyZUnivers
from datetime import date

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