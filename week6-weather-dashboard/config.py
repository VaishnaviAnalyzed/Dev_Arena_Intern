import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5"
CACHE_DIR = Path("data/cache")
FAVORITES_FILE = Path("data/favorites.json")

# Ensure directories exist
CACHE_DIR.mkdir(parents=True, exist_ok=True)