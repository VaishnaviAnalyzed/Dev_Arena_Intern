import sys
from .weather_api import WeatherAPI
from .weather_display import WeatherDisplay

def main():
    api = WeatherAPI()
    display = WeatherDisplay()
    city = "London"

    while True:
        current = api.fetch("weather", city)
        forecast = api.fetch("forecast", city)

        if current and forecast:
            display.show(current, forecast)
        else:
            print("City not found or API error.")

        cmd = input("\n[refresh | search <city> | quit]: ").lower().strip()
        if cmd == 'quit': break
        elif cmd.startswith('search '): city = cmd[7:]
        elif cmd == 'refresh': continue

if __name__ == "__main__":
    main()