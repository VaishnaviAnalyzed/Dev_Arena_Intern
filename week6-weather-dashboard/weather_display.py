from datetime import datetime

class WeatherDisplay:
    @staticmethod
    def get_icon(code: int) -> str:
        if 200 <= code < 300: return "⛈️"
        if 300 <= code < 600: return "🌧️"
        if 600 <= code < 700: return "❄️"
        if 800 == code: return "☀️"
        return "☁️"

    @classmethod
    def show(cls, current: dict, forecast: dict):
        print(f"\n📍 Location: {current['name']}, {current['sys']['country']}")
        print(f"🕐 Updated: {datetime.fromtimestamp(current['dt']).strftime('%H:%M:%S')}")
        print("─" * 30)
        
        # Current Weather
        w = current['weather'][0]
        m = current['main']
        print(f"Temp: {round(m['temp'])}°C | {w['description'].capitalize()} {cls.get_icon(w['id'])}")
        print(f"Wind: {round(current['wind']['speed'] * 3.6)} km/h | Humidity: {m['humidity']}%")
        
        # Forecast
        print("\n5-Day Forecast:")
        print("─" * 15)
        seen = set()
        for item in forecast['list']:
            d = datetime.fromtimestamp(item['dt'])
            day = d.strftime('%a %d')
            if day not in seen and d.hour >= 12:
                icon = cls.get_icon(item['weather'][0]['id'])
                print(f"{day}: {icon}  {round(item['main']['temp'])}°C")
                seen.add(day)
            if len(seen) == 5: break