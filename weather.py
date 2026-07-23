import requests

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

weather_data = get_weather(latitude=40.7128, longitude=-74.0060)

if weather_data:
    display_weather(weather_data)