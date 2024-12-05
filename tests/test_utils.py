from json import JSONDecodeError
import unittest
from unittest.mock import patch
from pyZUnivers import utils

class GetDatasTest(unittest.TestCase):

    @patch('pyZUnivers.utils.requests.get')
    def test_get_datas_success(self, mock_get):
        mock_response = {
            "key1": "value1",
            "key2": "value2"
        }
        mock_get.return_value.__enter__.return_value.json.return_value = mock_response

        url = "https://example.com/api"
        result = utils.get_datas(url)

        self.assertEqual(result, mock_response)

    @patch('pyZUnivers.utils.requests.get')
    def test_get_datas_json_decode_error(self, mock_get):
        mock_get.return_value.__enter__.return_value.json.side_effect = JSONDecodeError("", "", 0)

        url = "https://example.com/api"
        with self.assertRaises(utils.ZUniversAPIError):
            utils.get_datas(url)

    @patch('pyZUnivers.utils.requests.get')
    def test_get_datas_other_exception(self, mock_get):
        mock_get.return_value.__enter__.return_value.json.side_effect = Exception

        url = "https://example.com/api"
        with self.assertRaises(Exception):
            utils.get_datas(url)

class PostDatasTest(unittest.TestCase):

    @patch('pyZUnivers.utils.requests.post')
    def test_post_datas_success(self, mock_post):
        mock_response = {
            "key1": "value1",
            "key2": "value2"
        }
        mock_post.return_value.__enter__.return_value.json.return_value = mock_response

        url = "https://example.com/api"
        result = utils.post_datas(url)

        self.assertEqual(result, mock_response)

    @patch('pyZUnivers.utils.requests.post')
    def test_post_datas_json_decode_error(self, mock_post):
        mock_post.return_value.__enter__.return_value.json.side_effect = JSONDecodeError("", "", 0)

        url = "https://example.com/api"
        with self.assertRaises(utils.ZUniversAPIError):
            utils.post_datas(url)

    @patch('pyZUnivers.utils.requests.post')
    def test_post_datas_other_exception(self, mock_post):
        mock_post.return_value.__enter__.return_value.json.side_effect = Exception

        url = "https://example.com/api"
        with self.assertRaises(Exception):
            utils.post_datas(url)

class ParseUsernameTest(unittest.TestCase):

    def test_parse_username_with_valid_username(self):
        username = "john#123"
        expected_result = ("john#123", "john%23123")

        result = utils.parse_username(username)

        self.assertEqual(result, expected_result)

    def test_parse_username_with_empty_username(self):
        username = ""
        expected_result = ("", "")

        result = utils.parse_username(username)

        self.assertEqual(result, expected_result)

    def test_parse_username_with_none_username(self):
        username = None
        expected_result = (None, "")

        result = utils.parse_username(username)

        self.assertEqual(result, expected_result)
        
class IsAdventCalendarTest(unittest.TestCase):

    def test_is_advent_calendar_on_december(self):
        with patch('pyZUnivers.utils.datetime') as mock_datetime:
            mock_datetime.now.return_value.strftime.return_value = "01-12"
            result = utils.is_advent_calendar()
            self.assertTrue(result)

    def test_is_advent_calendar_on_january(self):
        with patch('pyZUnivers.utils.datetime') as mock_datetime:
            mock_datetime.now.return_value.strftime.return_value = "01-01"
            result = utils.is_advent_calendar()
            self.assertFalse(result)

    def test_is_advent_calendar_on_other_month(self):
        with patch('pyZUnivers.utils.datetime') as mock_datetime:
            mock_datetime.now.return_value.strftime.return_value = "01-07"
            result = utils.is_advent_calendar()
            self.assertFalse(result)
            
class GetAscensionLeaderboardTest(unittest.TestCase):

    @patch('pyZUnivers.utils.get_datas')
    def test_get_ascension_leaderboard_with_single_username(self, mock_get_datas):
        mock_response = {
            "users": [
                {
                    "maxFloorIndex": 5,
                    "towerLogCount": 18
                }
            ]
        }
        mock_get_datas.return_value = mock_response

        usernames = ["john#123"]
        result = utils.get_ascension_leaderboard(*usernames)
        expected = [
            {
                "maxFloorIndex": 6,
                "towerLogCount": 18
            }
        ]

        self.assertEqual(result, expected)

    @patch('pyZUnivers.utils.get_datas')
    def test_get_ascension_leaderboard_with_multiple_usernames(self, mock_get_datas):
        mock_response = {
            "users": [
                {
                    "maxFloorIndex": 5,
                    "towerLogCount": 18
                },
                {
                    "maxFloorIndex": 4,
                    "towerLogCount": 10
                },
                {
                    "maxFloorIndex": 5,
                    "towerLogCount": 6
                }
            ]
        }
        mock_get_datas.return_value = mock_response

        usernames = ["john#123", "jane#456", "doe#789"]
        result = utils.get_ascension_leaderboard(*usernames)
        expected = [
            {
                "maxFloorIndex": 6,
                "towerLogCount": 6
            },
            {
                "maxFloorIndex": 6,
                "towerLogCount": 18
            },
            {
                "maxFloorIndex": 5,
                "towerLogCount": 10
            }
        ]

        self.assertEqual(result, expected)

    @patch('pyZUnivers.utils.get_datas')
    def test_get_ascension_leaderboard_with_empty_usernames(self, mock_get_datas):
        mock_response = {
            "users": []
        }
        mock_get_datas.return_value = mock_response

        usernames = []
        result = utils.get_ascension_leaderboard(*usernames)

        self.assertEqual(result, mock_response["users"])
        
class GetInventoryTest(unittest.TestCase):

    @patch('pyZUnivers.utils.get_datas')
    def test_get_inventory_without_search(self, mock_get_datas):
        mock_response = [
            {
                "item": {
                    "id": 1,
                    "name": "Item 1",
                    "score": 10,
                    "isGolden": False
                },
                "quantity": 5
            },
            {
                "item": {
                    "id": 2,
                    "name": "Item 2",
                    "score": 20,
                    "shinyLevel": 1
                },
                "quantity": 3
            }
        ]
        mock_get_datas.return_value = mock_response

        username = "john#123"
        result = utils.get_inventory(username)

        self.assertEqual(result, mock_response)

    @patch('pyZUnivers.utils.get_datas')
    def test_get_inventory_with_search(self, mock_get_datas):
        mock_response = [
            {
                "item": {
                    "id": 1,
                    "name": "Item 1",
                    "score": 10,
                    "isGolden": False
                },
                "quantity": 5
            }
        ]
        mock_get_datas.return_value = mock_response

        username = "john#123"
        search = "Item 1"
        result = utils.get_inventory(username, search)

        self.assertEqual(result, mock_response)
        
class BestInventoryTest(unittest.TestCase):

    @patch('pyZUnivers.utils.get_inventory')
    def test_best_inventory_with_default_limit(self, mock_get_inventory):
        mock_response = [
            {
                "item": {
                    "id": 1,
                    "name": "Item 1",
                    "scores": {
                        "0": 10,
                        "1": 20,
                        "2": 30
                    }
                },
                "quantity": 5,
                "shinyLevel": 0
            },
            {
                "item": {
                    "id": 2,
                    "name": "Item 2",
                    "scores": {
                        "0": 20,
                        "1": 40,
                        "2": 60
                    },
                },
                "quantity": 3,
                "shinyLevel": 1
            },
            {
                "item": {
                    "id": 3,
                    "name": "Item 3",
                    "scores": {
                        "0": 15,
                        "1": 30,
                        "2": 45
                    }
                },
                "quantity": 2,
                "shinyLevel": 0
            }
        ]
        mock_get_inventory.return_value = mock_response

        username = "john#123"
        result = utils.best_inventory(username)

        expected = [
            {
                "item": {
                    "id": 2,
                    "name": "Item 2",
                    "scores": {
                        "0": 20,
                        "1": 40,
                        "2": 60
                    },
                },
                "quantity": 3,
                "shinyLevel": 1
            },
            {
                "item": {
                    "id": 3,
                    "name": "Item 3",
                    "scores": {
                        "0": 15,
                        "1": 30,
                        "2": 45
                    }
                },
                "quantity": 2,
                "shinyLevel": 0
            },
            {
                "item": {
                    "id": 1,
                    "name": "Item 1",
                    "scores": {
                        "0": 10,
                        "1": 20,
                        "2": 30
                    }
                },
                "quantity": 5,
                "shinyLevel": 0
            }
        ]

        self.assertEqual(result, expected)

    @patch('pyZUnivers.utils.get_inventory')
    def test_best_inventory_with_custom_limit(self, mock_get_inventory):
        mock_response = [
            {
                "item": {
                    "id": 1,
                    "name": "Item 1",
                    "scores": {
                        "0": 10,
                        "1": 20,
                        "2": 30
                    },
                },
                "quantity": 5,
                "shinyLevel": 0
            },
            {
                "item": {
                    "id": 2,
                    "name": "Item 2",
                    "scores": {
                        "0": 20,
                        "1": 40,
                        "2": 60
                    },
                },
                "quantity": 3,
                "shinyLevel": 1
            },
            {
                "item": {
                    "id": 3,
                    "name": "Item 3",
                    "scores": {
                        "0": 15,
                        "1": 30,
                        "2": 45
                    },
                },
                "quantity": 2,
                "shinyLevel": 0
            }
        ]
        mock_get_inventory.return_value = mock_response

        username = "john#123"
        limit = 2
        result = utils.best_inventory(username, limit)

        expected = [
            {
                "item": {
                    "id": 2,
                    "name": "Item 2",
                    "scores": {
                        "0": 20,
                        "1": 40,
                        "2": 60
                    },
                },
                "quantity": 3,
                "shinyLevel": 1
            },
            {
                "item": {
                    "id": 3,
                    "name": "Item 3",
                    "scores": {
                        "0": 15,
                        "1": 30,
                        "2": 45
                    },
                },
                "quantity": 2,
                "shinyLevel": 0
            }
        ]

        self.assertEqual(result, expected)
        
class GetCorrectDatetimeFormatTest(unittest.TestCase):

    def test_get_correct_datetime_format_with_microseconds(self):
        date = "2022-01-01T12:34:56.789"
        expected_result = "%Y-%m-%dT%H:%M:%S.%f"

        result = utils.get_correct_datetime_format(date)

        self.assertEqual(result, expected_result)

    def test_get_correct_datetime_format_without_microseconds(self):
        date = "2022-01-01T12:34:56"
        expected_result = "%Y-%m-%dT%H:%M:%S"

        result = utils.get_correct_datetime_format(date)

        self.assertEqual(result, expected_result)