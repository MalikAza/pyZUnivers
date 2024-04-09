import unittest
import pyZUnivers
from pyZUnivers.banners import UserBanner
from pyZUnivers.leaderboards import UserLeaderboards, _LeaderBoard
from pyZUnivers.subscription import Subscription

class UserBaseTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.powaza = pyZUnivers.User('powaza')
        self.powi_aza = pyZUnivers.User('powi_aza')
        self.hitsu = pyZUnivers.User('hitsumo')

    def test_url(self) -> None:
        self.assertIsInstance(self.powaza.url, str)

    def test_id(self) -> None:
        self.assertIsInstance(self.powaza.id, str)

    def test_discord_id(self) -> None:
        self.assertIsInstance(self.powaza.discord_id, str)

    def test_discord_avatar(self) -> None:
        self.assertIsInstance(self.powaza.discord_avatar, str)

    def test_balance(self) -> None:
        self.assertIsInstance(self.powaza.balance, int)

    def test_lore_dust(self) -> None:
        self.assertIsInstance(self.powaza.lore_dust, int)

    def test_lore_fragment(self) -> None:
        self.assertIsInstance(self.powaza.lore_fragment, int)

    def test_upgrade_dust(self) -> None:
        self.assertIsInstance(self.powaza.upgrade_dust, int)

    def test_rank(self) -> None:
        self.assertIsInstance(self.powaza.rank, str)

    def test_banner(self) -> None:
        self.assertIsInstance(self.powaza.banner, UserBanner)

        self.assertIsInstance(self.powaza.banner.date, str)
        self.assertIsInstance(self.powaza.banner.image_url, str)
        self.assertIsInstance(self.powaza.banner.title, str)

    def test_is_active(self) -> None:
        self.assertEqual(self.powaza.is_active, True)
        self.assertEqual(self.powi_aza.is_active, False)

    def test_leaderboards(self) -> None:
        self.assertIsInstance(self.powaza.leaderboards, UserLeaderboards)

        self.assertIsInstance(self.powaza.leaderboards.tradeless, _LeaderBoard)
        self.assertAlmostEqual(self.hitsu.leaderboards.tradeless, False)
        
        self.assertIsInstance(self.powaza.leaderboards.constellations, _LeaderBoard)
        self.assertEqual(self.powi_aza.leaderboards.constellations, False)

    def test_cards(self) -> None:
        self.assertIsInstance(self.powaza.cards, int)

    def test_unique_cards(self) -> None:
        self.assertEqual(
            '/' in self.powaza.unique_cards, True
        )

        splited = self.powaza.unique_cards.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)

    def test_unique_golden_cards(self) -> None:
        self.assertEqual(
            '/' in self.powaza.unique_golden_cards, True
        )

        splited = self.powaza.unique_golden_cards.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)

    def test_unique_constellation_cards(self) -> None:
        self.assertEqual(
            '/' in self.powaza.unique_constellation_cards, True
        )

        splited = self.powaza.unique_constellation_cards.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)

    def test_unique_golden_constellation_cards(self) -> None:
        self.assertEqual(
            '/' in self.powaza.unique_golden_constellation_cards, True
        )

        splited = self.powaza.unique_golden_constellation_cards.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)

    def test_tickets(self) -> None:
        self.assertIsInstance(self.powaza.tickets, int)

    def test_achievements(self) -> None:
        self.assertEqual(
            '/' in self.powaza.achievements, True
        )

        splited = self.powaza.achievements.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)

    def test_subscription(self) -> None:
        self.assertTrue(
            isinstance(self.powaza.subscription, Subscription)
            or
            self.powaza.subscription == False
        )

    def test_today_trades(self) -> None:
        self.assertEqual(
            '/' in self.powaza.today_trades, True
        )

        splited = self.powaza.today_trades.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)

    def test_subscription_bonus(self) -> None:
        self.assertEqual(
            '/' in self.powaza.subscription_bonus, True
        )

        splited = self.powaza.subscription_bonus.split('/')
        self.assertEqual(len(splited), 2)

        [count, total] = [int(x) for x in splited]
        self.assertIsInstance(count, int)
        self.assertIsInstance(total, int)

if __name__ == '__main__':
    unittest.main()