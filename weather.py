import requests

def get_coordinates(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    parameters = {
        "name": city
    }

    try:
        response = requests.get(url, params=parameters)
        response.raise_for_status()

    except:
        print("Error: Unable to retrieve coordinates.")
        return None

    data = response.json()

    if "results" not in data or not data["results"]:
        return None

    return {
        "latitude": data["results"][0]["latitude"],
        "longitude": data["results"][0]["longitude"]
    }

def get_weather(latitude, longitude):

    url = "https://api.open-meteo.com/v1/forecast"

    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    try:
        response = requests.get(url, params=parameters)
        response.raise_for_status()

    except:
        print("Error: Unable to retrieve weather data.")
        return None

    data = response.json()

    return data

def display_weather(data):

    temperature_celsius = data["current_weather"]["temperature"]
    temperature_fahrenheit = temperature_celsius * 9/5 + 32

    wind_speed_kmh = data["current_weather"]["windspeed"]
    wind_speed_mph = wind_speed_kmh * 0.6213712

    print(f"Current Temperature: {round(temperature_fahrenheit)}°F")
    print(f"Current Wind Speed: {round(wind_speed_mph, 1)} mph")

def main():
    print("Enter a city name to get the current weather:")

    city = input()

    coordinates = get_coordinates(city)

    if coordinates is None:
        print("Error: Unable to retrieve coordinates for the specified city.")
        return

    weather_data = get_weather(
        latitude=coordinates["latitude"], 
        longitude=coordinates["longitude"])

    if weather_data:
        display_weather(weather_data)

main()