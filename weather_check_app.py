import requests
import argparse
import time
from favorites_manager import add_favorite, remove_favorite, list_favorites,load_favorites

API_KEY = "715eed1574f8453c9bf133352230411"  # Replace with your WeatherAPI.com API key

def get_weather(city, unit):
    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "q": city,
        "key": API_KEY,
        "unit": unit
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if "error" in data:
        return f"Could not fetch weather data for {city}."
    else:
        weather_description = data["current"]["condition"]["text"]
        temperature = data["current"]["temp_c"] if unit == "C" else data["current"]["temp_f"]
        return f"Weather in {city}: {weather_description}\nTemperature: {temperature}°{unit}"

def get_weather_for_favorites(favorites, unit):
    for city in favorites:
        print(get_weather(city, unit))
        print("-" * 30)

def main():
    parser = argparse.ArgumentParser(description="Weather Checking Application")
    parser.add_argument("city", nargs="?", help="City for which you want to check the weather")
    parser.add_argument(
        "--unit",
        choices=["C", "F"],
        default="C",
        help="Temperature unit (Celsius or Fahrenheit)",
    )
    parser.add_argument(
        "--addfavorites",
        action="store_true",
        help="Add this city to favorites",
    )
    parser.add_argument(
        "--removefavorites",
        action="store_true",
        help="Remove the city from favorites"
    )
    parser.add_argument(
        "--listfavorites",
        action="store_true",
        help="List the favorites cities",
    )
    parser.add_argument(
        "--getweatherfavorites",
        action="store_true",
        help="Display weather for favorite cities",
    )

    args = parser.parse_args()

    if args.addfavorites:
        if args.city:
            add_favorite(args.city)
        else:
            print("Enter city to be added.")
    elif args.removefavorites:
        if args.city:
            remove_favorite(args.city)
        else:
            print("Enter city to be removed.")
    elif args.listfavorites:
        list_favorites()
    elif args.getweatherfavorites:
        favorites = load_favorites()
        while True:
            if favorites:
                get_weather_for_favorites(favorites, args.unit)
            else:
                print("Your favorites list is empty.")
            time.sleep(15) 
    else:
        while True:
            if args.city:
                print(get_weather(args.city, args.unit))
            else:
                print("Please specify a city or use the --favorites option to see your favorite cities.")
            time.sleep(15)  # Auto-refresh every 15 seconds

if __name__ == "__main__":
    main()