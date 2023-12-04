import unittest
import pyZUnivers
from typing import List, Union
from datetime import datetime
from pyZUnivers.pins import UserPin
from pyZUnivers.pack import Pack

class UserOverviewTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.overview_powaza = pyZUnivers.UserOverview('powaza')

    def test_overview(self) -> None:
        self.assertIsInstance(self.overview_powaza, pyZUnivers.UserOverview)

    def test_pins(self) -> None:
        self.assertIsInstance(self.overview_powaza.pins, List)
        for pin in self.overview_powaza.pins:
            self.assertIsInstance(pin, UserPin)
            self.assertIsInstance(pin.id, str)
            self.assertIsInstance(pin.name, str)
            self.assertIsInstance(pin.type, str)
            self.assertIsInstance(pin.rarity, int)
            self.assertIsInstance(pin.identifier, int)
            self.assertIsInstance(pin.description, Union[str, None])
            self.assertIsInstance(pin.reference, Union[str, None])
            self.assertIsInstance(pin.pack, Pack)
            self.assertIsInstance(pin.image_urls, List)
            for url in pin.image_urls:
                self.assertIsInstance(url, str)
            self.assertIsInstance(pin.score, int)
            self.assertIsInstance(pin.score_golden, int)
            self.assertIsInstance(pin.is_recyclable, bool)
            self.assertIsInstance(pin.is_tradable, bool)
            self.assertIsInstance(pin.is_counting, bool)
            self.assertIsInstance(pin.is_craftable, bool)
            self.assertIsInstance(pin.is_invocable, bool)
            self.assertIsInstance(pin.is_goldable, bool)
            self.assertIsInstance(pin.is_upgradable, bool)
            self.assertIsInstance(pin.is_golden, bool)

    def test_invocations_before_pity(self) -> None:
        self.assertIsInstance(self.overview_powaza.invocations_before_pity, int)

    def test_vortex_name(self) -> None:
        self.assertIsInstance(self.overview_powaza.vortex_name, str)

    def test_vortex_start_date(self) -> None:
        self.assertIsInstance(self.overview_powaza.vortex_start_date, datetime)

    def test_vortex_end_date(self) -> None:
        self.assertIsInstance(self.overview_powaza.vortex_end_date, datetime)

    def test_vortex_floor(self) -> None:
        self.assertIsInstance(self.overview_powaza.vortex_floor, int)

    def test_vortex_tries(self) -> None:
        self.assertIsInstance(self.overview_powaza.vortex_tries, int)