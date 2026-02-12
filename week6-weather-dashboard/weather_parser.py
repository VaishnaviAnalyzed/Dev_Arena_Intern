from datetime import datetime

class WeatherParser:
    """Cleans and structures raw API data for the display."""
    
    @staticmethod
    def parse_current(data: dict) -> dict:
        return {
            "city": data.get("name"),
            "country": data.get("sys", {}).get("country"),
            "temp": round(data["main"]["temp"]),
            "feels_like": round(data["main"]["feels_like"]),
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].capitalize(),
            "wind_speed": round(data["wind"]["speed"] * 3.6),  # km/h
            "icon_id": data["weather"][0]["id"],
            "timestamp": datetime.fromtimestamp(data["dt"]).strftime('%Y-%m-%d %H:%M:%S')
        }

    @staticmethod
    def parse_forecast(data: dict) -> list:
        parsed_forecast = []
        seen_days = set()
        
        for entry in data.get("list", []):
            dt = datetime.fromtimestamp(entry["dt"])
            day_key = dt.strftime('%a %d %b')
            
            # Pick the entry closest to Midday for the daily forecast
            if day_key not in seen_days and dt.hour >= 12:
                parsed_forecast.append({
                    "day": day_key,
                    "temp": round(entry["main"]["temp"]),
                    "icon_id": entry["weather"][0]["id"],
                    "humidity": entry["main"]["humidity"]
                })
                seen_days.add(day_key)
        return parsed_forecast[:5]