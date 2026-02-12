import unittest
from unittest.mock import patch, MagicMock
from .weather_api import WeatherAPI

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        self.api = WeatherAPI()

    @patch('requests.get')
    def test_fetch_success(self, mock_get):
        # Mocking a successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"name": "London", "main": {"temp": 15}}
        mock_get.return_value = mock_response

        result = self.api.fetch("weather", "London")
        self.assertEqual(result["name"], "London")
        self.assertEqual(result["main"]["temp"], 15)

    def test_cache_logic(self):
        # Manually save a fake cache
        test_data = {"test": "data"}
        self.api._save_cache("test_key", test_data)
        
        cached = self._get_cache("test_key")
        self.assertEqual(cached, test_data)