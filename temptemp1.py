import pip

def install(package):
    pip.main(['install', package])

try:
    import requests
except ImportError:
    install('requests')
    import requests
import json

def get_weather_forecast(city):
    """Gets the current weather forecast for a city.

    Args:
        city: The name of the city to get the weather forecast for.

    Returns:
        A dictionary containing the current weather forecast for the city.
    """

    api_key = ""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise Exception(f"Error getting weather forecast for {city}: {data['message']}")

    return data

def main():
    """The main function."""

    city = input("Enter a city name: ")
    weather_forecast = get_weather_forecast(city)

    print(f"Current weather forecast for {city}:")
    print(f"* Temperature: {weather_forecast['main']['temp']}°C")
    print(f"* Description: {weather_forecast['weather'][0]['description']}")

if __name__ == "__main__":
    main()