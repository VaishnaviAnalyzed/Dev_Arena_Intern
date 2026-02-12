# Weather Dashboard Application 
## Project Description 
A comprehensive weather application that fetches real-time weather data from external APIs and displays it in a user-friendly interface. This project demonstrates API integration, external library usage, and professional Python development practices. 

## What I Learned 
1. **API Integration**: How to work with external web services
2. **HTTP Requests**: Making GET requests and handling responses
3. **JSON Processing**: Parsing and working with complex JSON data.
4. **Error Handling**: Managing network errors and API limitations
5. **Environment Management**: Using environment variables for configuration
6. **Package Management**: Installing and using external libraries
  

## Features 
- ✅ Current weather for any city worldwide
- ✅ 5-day weather forecast with daily summaries
- ✅ Temperature in Celsius or Fahrenheit
- ✅ Weather condition icons and descriptions
- ✅ Wind speed, humidity, and pressure information
- ✅ City search with autocomplete
- ✅ Favorite cities management
- ✅ API response caching
- ✅ Comprehensive error handling
- ✅ Export weather data to CSV


## How to Run 
1. Get API key from OpenWeatherMap
2. Copy .env.example to .env and add your API key
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python -m weather_app.main`


## Required Libraries 
- requests: For making HTTP requests
- python-dotenv: For environment variable management
- colorama: For colored terminal output (optional)

## Sample Output 
```
🌤️ WEATHER DASHBOARD
======================= 
📍 Current Location: New York, US
🕐 Last Updated: 2024-01-25 14:30:00

Current Weather:
────────────────
Temperature: 12°C (Feels like: 10°C)
Conditions: Few clouds ☁️
Humidity: 65%
Wind: 15 km/h from NW
Pressure: 1013 hPa
Visibility: 10 km

5-Day Forecast:
───────────────
Thu 25 Jan: ☀️ 14°C / 8°C
Fri 26 Jan: 🌤️ 13°C / 7°C
Sat 27 Jan: 🌧️ 11°C / 6°C
Sun 28 Jan: ⛅ 12°C / 7°C
Mon 29 Jan: ☀️ 15°C / 9°C

Search city or command (help/quit/favorites):
```
