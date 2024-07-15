import unittest
from datetime import datetime
from pyZUnivers.vortex import Vortex, _FloorsDropRates, _FloorIndexError

class VortexTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.__vortex = Vortex()

    def test_name(self) -> None:
        self.assertIsInstance(self.__vortex.name, str)

    def test_pack_name(self) -> None:
        self.assertIsInstance(self.__vortex.pack_name, str)

    def test_pack_year(self) -> None:
        self.assertIsInstance(self.__vortex.pack_year, int|None)

    def test_reputation_name(self) -> None:
        self.assertIsInstance(self.__vortex.reputation_name, str)

    def test_begin_date(self) -> None:
        self.assertIsInstance(self.__vortex.begin_date, datetime)

    def test_end_date(self) -> None:
        self.assertIsInstance(self.__vortex.end_date, datetime)

    def test_floor_drop_rates(self) -> None:
        # Negative normal number
        self.assertIsInstance(
            self.__vortex.get_floor_drop_rates(-1), _FloorsDropRates
        )
        # Negative number too high
        self.assertRaises(
            _FloorIndexError, lambda: self.__vortex.get_floor_drop_rates(-10)
        )
        # Positive normal number
        self.assertIsInstance(
            self.__vortex.get_floor_drop_rates(1), _FloorsDropRates
        )
        # Positive number too high
        self.assertRaises(
            _FloorIndexError, lambda: self.__vortex.get_floor_drop_rates(10)
        )
        # _FloorsDropRates tests
        floor_rates = self.__vortex.get_floor_drop_rates(1)
            # rarity one normal
        self.assertEqual(
            '%' in floor_rates.rarity_one_normal, True
        )
        self.assertIsInstance(
            int(floor_rates.rarity_one_normal.removesuffix('.0%')), int
        )
            # rarity one golden
        self.assertEqual(
            '%' in floor_rates.rarity_one_golden, True
        )
        self.assertIsInstance(
            int(floor_rates.rarity_one_golden.removesuffix('.0%')), int
        )
            # rarity two normal
        self.assertEqual(
            '%' in floor_rates.rarity_two_normal, True
        )
        self.assertIsInstance(
            int(floor_rates.rarity_two_normal.removesuffix('.0%')), int
        )
            # rarity two golden
        self.assertEqual(
            '%' in floor_rates.rarity_two_golden, True
        )
        self.assertIsInstance(
            int(floor_rates.rarity_two_golden.removesuffix('.0%')), int
        )
            # rarity three normal
        self.assertEqual(
            '%' in floor_rates.rarity_three_normal, True
        )
        self.assertIsInstance(
            int(floor_rates.rarity_three_normal.removesuffix('.0%')), int
        )
            # rarity three golden
        self.assertEqual(
            '%' in floor_rates.rarity_three_golden, True
        )
        self.assertIsInstance(
            int(floor_rates.rarity_three_golden.removesuffix('.0%')), int
        )
            # rarity four normal
        self.assertEqual(
            '%' in floor_rates.rarity_four_normal, True
        )
        self.assertIsInstance(
            int(floor_rates.rarity_four_normal.removesuffix('.0%')), int
        )
            # rarity four golden
        self.assertEqual(
            '%' in floor_rates.rarity_four_golden, True
        )
        self.assertIsInstance(
            int(floor_rates.rarity_four_golden.removesuffix('.0%')), int
        )