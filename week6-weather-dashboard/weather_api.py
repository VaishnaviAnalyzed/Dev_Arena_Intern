import requests
import json
import time
from typing import Optional, Dict
from .config import API_KEY, BASE_URL, CACHE_DIR

class WeatherAPI:
    def __init__(self):
        self.cache_duration = 600

    def _get_cache(self, key: str) -> Optional[Dict]:
        path = CACHE_DIR / f"{key}.json"
        if path.exists() and (time.time() - path.stat().st_mtime < self.cache_duration):
            return json.loads(path.read_text())
        return None

    def _save_cache(self, key: str, data: Dict):
        (CACHE_DIR / f"{key}.json").write_text(json.dumps(data, indent=2))

    def fetch(self, endpoint: str, city: str) -> Optional[Dict]:
        cache_key = f"{endpoint}_{city.replace(' ', '_')}"
        cached = self._get_cache(cache_key)
        if cached: return cached

        params = {"q": city, "appid": API_KEY, "units": "metric"}
        try:
            resp = requests.get(f"{BASE_URL}/{endpoint}", params=params, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                self._save_cache(cache_key, data)
                return data
        except Exception as e:
            print(f"Connection Error: {e}")
        return None