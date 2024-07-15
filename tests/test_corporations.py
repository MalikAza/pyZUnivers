import unittest
from datetime import datetime
from pyZUnivers.corporations import Corporation, CorporationBonuses, CorporationDonation, CorporationMember

class CorporationTest(unittest.TestCase):

    def setUp(self):
        self.corporation_payload = {
            'id': '123',
            'name': 'Test Corporation',
            'description': 'This is a test corporation',
            'balance': 1000,
            'logoUrl': 'https://example.com/logo.png',
            'logoFileName': 'logo.png',
            'createdDate': '2022-01-01T00:00:00',
            'modifiedDate': '2022-01-02T00:00:00',
            'corporationBonuses': [
                {'type': 'MEMBER_COUNT', 'level': 2},
                {'type': 'LOOT', 'level': 3},
                {'type': 'RECYCLE_LORE_DUST', 'level': 1},
                {'type': 'RECYCLE_LORE_FRAGMENT', 'level': 2}
            ],
            'corporationLedgers': [
                {
                    'amount': 100,
                    'date': '2022-01-01T10:00:00',
                    'user': {'discordUsername': 'User1', 'discordId': 123},
                    'role': 'ADMIN'
                },
                {
                    'amount': 200,
                    'date': '2022-01-02T10:00:00',
                    'user': {'discordUsername': 'User2', 'discordId': 456},
                    'role': 'MEMBER'
                }
            ],
            'userCorporations': [
                {
                    'user': {'discordId': 123, 'discordUsername': 'User1'},
                    'role': 'ADMIN',
                    'joinedDate': '2022-01-01T00:00:00',
                    'giveToday': 50,
                    'giveTotal': 150
                },
                {
                    'user': {'discordId': 456, 'discordUsername': 'User2'},
                    'role': 'MEMBER',
                    'joinedDate': '2022-01-02T00:00:00',
                    'giveToday': 100,
                    'giveTotal': 200
                }
            ]
        }

        self.corporation = Corporation(self.corporation_payload)

    def test_id(self):
        self.assertEqual(self.corporation.id, '123')

    def test_name(self):
        self.assertEqual(self.corporation.name, 'Test Corporation')

    def test_description(self):
        self.assertEqual(self.corporation.description, 'This is a test corporation')

    def test_balance(self):
        self.assertEqual(self.corporation.balance, 1000)

    def test_logo_url(self):
        self.assertEqual(self.corporation.logo_url, 'https://example.com/logo.png')

    def test_logo_file_name(self):
        self.assertEqual(self.corporation.logo_file_name, 'logo.png')

    def test_created_date(self):
        expected_date = datetime(2022, 1, 1, 0, 0, 0)
        self.assertEqual(self.corporation.created_date, expected_date)

    def test_modified_date(self):
        expected_date = datetime(2022, 1, 2, 0, 0, 0)
        self.assertEqual(self.corporation.modified_date, expected_date)

    def test_bonuses(self):
        bonuses = self.corporation.bonuses
        self.assertIsInstance(bonuses, CorporationBonuses)
        self.assertEqual(bonuses.member_count.level, 2)
        self.assertEqual(bonuses.loot.level, 3)
        self.assertEqual(bonuses.recycle_lore_dust.level, 1)
        self.assertEqual(bonuses.recycle_lore_fragment.level, 2)

    def test_donations(self):
        donations = self.corporation.donations
        self.assertIsInstance(donations, list)
        self.assertEqual(len(donations), 2)

        donation1 = donations[0]
        self.assertIsInstance(donation1, CorporationDonation)
        self.assertEqual(donation1.amount, 100)
        self.assertEqual(donation1.date, datetime(2022, 1, 1, 10, 0, 0))
        self.assertEqual(donation1.user_name, 'User1')
        self.assertEqual(donation1.user_id, 123)
        self.assertEqual(donation1.user_role, 'PDG')

        donation2 = donations[1]
        self.assertIsInstance(donation2, CorporationDonation)
        self.assertEqual(donation2.amount, 200)
        self.assertEqual(donation2.date, datetime(2022, 1, 2, 10, 0, 0))
        self.assertEqual(donation2.user_name, 'User2')
        self.assertEqual(donation2.user_id, 456)
        self.assertEqual(donation2.user_role, 'Membre')

    def test_members(self):
        members = self.corporation.members
        self.assertIsInstance(members, list)
        self.assertEqual(len(members), 2)

        member1 = members[0]
        self.assertIsInstance(member1, CorporationMember)
        self.assertEqual(member1.id, 123)
        self.assertEqual(member1.name, 'User1')
        self.assertEqual(member1.role, 'PDG')
        self.assertEqual(member1.joined_date, datetime(2022, 1, 1, 0, 0, 0))
        self.assertEqual(member1.today_donations, 50)
        self.assertEqual(member1.total_donations, 150)

        member2 = members[1]
        self.assertIsInstance(member2, CorporationMember)
        self.assertEqual(member2.id, 456)
        self.assertEqual(member2.name, 'User2')
        self.assertEqual(member2.role, 'Membre')
        self.assertEqual(member2.joined_date, datetime(2022, 1, 2, 0, 0, 0))
        self.assertEqual(member2.today_donations, 100)
        self.assertEqual(member2.total_donations, 200)

    def test_url(self):
        self.assertEqual(self.corporation.url, 'https://zunivers.zerator.com/corporation/123')

if __name__ == '__main__':
    unittest.main()