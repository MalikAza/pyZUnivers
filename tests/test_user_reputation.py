import unittest
from pyZUnivers.reputation import UserReputation, _ReputationClan

class UserReputationTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.__reput_powaza = UserReputation('powaza')

    def test_first(self) -> None:
        self.assertIsInstance(self.__reput_powaza.first, _ReputationClan)
        self.assertIsInstance(self.__reput_powaza.first.name, str)
        self.assertIsInstance(self.__reput_powaza.first.level_name, str)

        self.assertEqual(
            '/' in self.__reput_powaza.first.progress, True
        )

        splited = self.__reput_powaza.first.progress.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)

    def test_second(self) -> None:
        self.assertIsInstance(self.__reput_powaza.second, _ReputationClan)
        self.assertIsInstance(self.__reput_powaza.second.name, str)
        self.assertIsInstance(self.__reput_powaza.second.level_name, str)

        self.assertEqual(
            '/' in self.__reput_powaza.second.progress, True
        )

        splited = self.__reput_powaza.second.progress.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)

    def test_third(self) -> None:
        self.assertIsInstance(self.__reput_powaza.third, _ReputationClan)
        self.assertIsInstance(self.__reput_powaza.third.name, str)
        self.assertIsInstance(self.__reput_powaza.third.level_name, str)

        self.assertEqual(
            '/' in self.__reput_powaza.third.progress, True
        )

        splited = self.__reput_powaza.third.progress.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)

    def test_fourth(self) -> None:
        self.assertIsInstance(self.__reput_powaza.fourth, _ReputationClan)
        self.assertIsInstance(self.__reput_powaza.fourth.name, str)
        self.assertIsInstance(self.__reput_powaza.fourth.level_name, str)

        self.assertEqual(
            '/' in self.__reput_powaza.fourth.progress, True
        )

        splited = self.__reput_powaza.fourth.progress.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)

    def test_fifth(self) -> None:
        self.assertIsInstance(self.__reput_powaza.fifth, _ReputationClan)
        self.assertIsInstance(self.__reput_powaza.fifth.name, str)
        self.assertIsInstance(self.__reput_powaza.fifth.level_name, str)

        self.assertEqual(
            '/' in self.__reput_powaza.fifth.progress, True
        )

        splited = self.__reput_powaza.fifth.progress.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)