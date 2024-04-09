import unittest
import pyZUnivers
from typing import Union
from pyZUnivers.challenges import _ChallengeAtrb
from datetime import datetime

class UserChallengesTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.__challenges = pyZUnivers.Challenges()

    def test_is_Challenge(self) -> None:
        self.assertIsInstance(self.__challenges, pyZUnivers.Challenges)

    def test_begin_date(self) -> None:
        self.assertIsInstance(self.__challenges.begin_date, datetime)

    def test_end_date(self) -> None:
        self.assertIsInstance(self.__challenges.end_date, datetime)

    def test_first(self) -> None:
        self.assertIsInstance(self.__challenges.first, _ChallengeAtrb)
        # === .progress === #
        self.assertEqual(
            '/' in self.__challenges.first.progress, True
        )

        splited = self.__challenges.first.progress.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)

        # === achieved_date === #
        self.assertIsInstance(self.__challenges.first.achieved_date, Union[None, datetime])

    def test_second(self) -> None:
        self.assertIsInstance(self.__challenges.second, _ChallengeAtrb)
        # === .progress === #
        self.assertEqual(
            '/' in self.__challenges.second.progress, True
        )

        splited = self.__challenges.second.progress.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)

        # === achieved_date === #
        self.assertIsInstance(self.__challenges.second.achieved_date, Union[None, datetime])

    def test_third(self) -> None:
        self.assertIsInstance(self.__challenges.third, _ChallengeAtrb)
        # === .progress === #
        self.assertEqual(
            '/' in self.__challenges.third.progress, True
        )

        splited = self.__challenges.third.progress.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)

        # === achieved_date === #
        self.assertIsInstance(self.__challenges.third.achieved_date, Union[None, datetime])