# weather_api.py
import requests
import json
from datetime import datetime
from pathlib import Path
import time
from typing import Optional, Dict

class WeatherAPI:
    def __init__(self, api_key: str, base_url: str = "http://api.openweathermap.org/data/2.5"):
        self.api_key = api_key
        self.base_url = base_url
        self.cache_dir = Path("data/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_duration = 600 

    def _get_cached_data(self, cache_key: str) -> Optional[Dict]:
        cache_file = self.cache_dir / f"{cache_key}.json"
        if cache_file.exists():
            if time.time() - cache_file.stat().st_mtime < self.cache_duration:
                with open(cache_file, 'r') as f:
                    return json.load(f)
        return None

    def _save_to_cache(self, cache_key: str, data: Dict):
        cache_file = self.cache_dir / f"{cache_key}.json"
        with open(cache_file, 'w') as f:
            json.dump(data, f, indent=2)

    def _make_request(self, endpoint: str, params: Dict) -> Optional[Dict]:
        try:
            params.update({'appid': self.api_key, 'units': 'metric'})
            response = requests.get(f"{self.base_url}/{endpoint}", params=params, timeout=10)
            if response.status_code == 200: return response.json()
            print(f"Error: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        return None

    def get_current_weather(self, city: str) -> Optional[Dict]:
        cache_key = f"current_{city.replace(' ', '_')}"
        cached = self._get_cached_data(cache_key)
        if cached: return cached
        
        data = self._make_request("weather", {'q': city})
        if data: self._save_to_cache(cache_key, data)
        return data

    def get_forecast(self, city: str) -> Optional[Dict]:
        cache_key = f"forecast_{city.replace(' ', '_')}"
        cached = self._get_cached_data(cache_key)
        if cached: return cached
        
        data = self._make_request("forecast", {'q': city})
        if data: self._save_to_cache(cache_key, data)
        return data

def get_icon(condition_code: int) -> str:
    """Returns an emoji based on OpenWeather condition codes"""
    if 200 <= condition_code < 300: return "⛈️"
    if 300 <= condition_code < 600: return "🌧️"
    if 600 <= condition_code < 700: return "❄️"
    if 800 == condition_code: return "☀️"
    return "☁️"

def display_dashboard(current: Dict, forecast: Dict):
    # Header logic
    name = current['name']
    country = current['sys']['country']
    dt = datetime.fromtimestamp(current['dt']).strftime('%Y-%m-%d %H:%M:%S')
    
    print("\nWEATHER DASHBOARD")
    print("=======================")
    print(f"📍 Current Location: {name}, {country}")
    print(f"🕐 Last Updated: {dt}")
    
    print("\nCurrent Weather:")
    print("────────────────")
    main = current['main']
    wind = current['wind']
    weather = current['weather'][0]
    
    print(f"Temperature:   {round(main['temp'])}°C (Feels like: {round(main['feels_like'])}°C)")
    print(f"Conditions:    {weather['description'].capitalize()} {get_icon(weather['id'])}")
    print(f"Humidity:      {main['humidity']}%")
    print(f"Wind:          {round(wind['speed'] * 3.6)} km/h") # Convert m/s to km/h
    print(f"Pressure:      {main['pressure']} hPa")
    
    print("\n5-Day Forecast:")
    print("───────────────")
    # Forecast data gives 3-hour chunks; we'll pick one per day (around noon)
    seen_days = set()
    for item in forecast['list']:
        date_obj = datetime.fromtimestamp(item['dt'])
        day_str = date_obj.strftime('%a %d %b')
        if day_str not in seen_days and date_obj.hour >= 12:
            icon = get_icon(item['weather'][0]['id'])
            temp = round(item['main']['temp'])
            hum = item['main']['humidity']
            print(f"{day_str}:  {icon}   {temp}°C  (Humidity: {hum}%)")
            seen_days.add(day_str)
        if len(seen_days) >= 5: break

def main():
    API_KEY = "YOUR API KEY"  # <--- Replace this
    api = WeatherAPI(API_KEY)
    current_city = "London"

    while True:
        current_data = api.get_current_weather(current_city)
        forecast_data = api.get_forecast(current_city)

        if current_data and forecast_data:
            display_dashboard(current_data, forecast_data)
        else:
            print("Failed to retrieve data. Check your API key or city name.")

        print("\nType 'refresh' to update, 'search [city]' for new city, or 'quit' to exit:")
        user_input = input("> ").strip().lower()

        if user_input == 'quit':
            break
        elif user_input.startswith('search '):
            current_city = user_input.replace('search ', '')
        elif user_input == 'refresh':
            continue

if __name__ == "__main__":
    main()
