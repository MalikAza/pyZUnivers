import unittest
import pyZUnivers
from typing import Union
from pyZUnivers.challenges import _ChallengeAtrb
from datetime import datetime

class UserChallengesTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.__powaza_challenges = pyZUnivers.Challenges('powaza')

    def test_is_Challenge(self) -> None:
        self.assertIsInstance(self.__powaza_challenges, pyZUnivers.Challenges)

    def test_begin_date(self) -> None:
        self.assertIsInstance(self.__powaza_challenges.begin_date, datetime)

    def test_end_date(self) -> None:
        self.assertIsInstance(self.__powaza_challenges.end_date, datetime)

    def test_first(self) -> None:
        self.assertIsInstance(self.__powaza_challenges.first, _ChallengeAtrb)
        # === .progress === #
        self.assertEqual(
            '/' in self.__powaza_challenges.first.progress or self.__powaza_challenges.first.progress == '✅', True
        )

        if '/' in self.__powaza_challenges.first.progress:
            splited = self.__powaza_challenges.first.progress.split('/')
            self.assertEqual(len(splited), 2)

            [count, total] = [int(x) for x in splited]
            self.assertIsInstance(count, int)
            self.assertIsInstance(total, int)

        # === achieved_date === #
        self.assertIsInstance(self.__powaza_challenges.first.achieved_date, Union[None, datetime])

    def test_second(self) -> None:
        self.assertIsInstance(self.__powaza_challenges.second, _ChallengeAtrb)
        # === .progress === #
        self.assertEqual(
            '/' in self.__powaza_challenges.second.progress or self.__powaza_challenges.second.progress == '✅', True
        )

        if '/' in self.__powaza_challenges.second.progress:
            splited = self.__powaza_challenges.second.progress.split('/')
            self.assertEqual(len(splited), 2)

            [count, total] = [int(x) for x in splited]
            self.assertIsInstance(count, int)
            self.assertIsInstance(total, int)

        # === achieved_date === #
        self.assertIsInstance(self.__powaza_challenges.second.achieved_date, Union[None, datetime])

    def test_third(self) -> None:
        self.assertIsInstance(self.__powaza_challenges.third, _ChallengeAtrb)
        # === .progress === #
        self.assertEqual(
            '/' in self.__powaza_challenges.third.progress or self.__powaza_challenges.third.progress == '✅', True
        )

        if '/' in self.__powaza_challenges.third.progress:
            splited = self.__powaza_challenges.third.progress.split('/')
            self.assertEqual(len(splited), 2)

            [count, total] = [int(x) for x in splited]
            self.assertIsInstance(count, int)
            self.assertIsInstance(total, int)

        # === achieved_date === #
        self.assertIsInstance(self.__powaza_challenges.third.achieved_date, Union[None, datetime])