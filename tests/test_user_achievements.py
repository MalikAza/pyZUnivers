import unittest
import pyZUnivers

class UserAchievementsTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.__powaza_achievements = pyZUnivers.Achievements('powaza')
        self.__malikaza_achievements = pyZUnivers.Achievements('malikaza')

    def test_is_Achievements(self) -> None:
        self.assertIsInstance(self.__powaza_achievements, pyZUnivers.Achievements)

    def test_get_yearly_is_false(self) -> None:
        self.assertFalse(self.__powaza_achievements.get_yearly(1))

    def test_get_yearly_is_int(self) -> None:
        self.assertIsInstance(self.__malikaza_achievements.get_yearly(3), int)