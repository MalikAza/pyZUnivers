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