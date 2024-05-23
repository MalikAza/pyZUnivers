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