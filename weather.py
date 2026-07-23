import requests

url = "https://api.open-meteo.com/v1/forecast"

parameters = {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "current_weather": True
}

response = requests.get(url, params=parameters)

data = response.json()

temperature_celsius = data["current_weather"]["temperature"]
temperature_fahrenheit = temperature_celsius * 9/5 + 32

wind_speed_kmh = data["current_weather"]["windspeed"]
wind_speed_mph = wind_speed_kmh * 0.6213712

print(f"Current Temperature: {round(temperature_fahrenheit)}°F")
print(f"Current Wind Speed: {round(wind_speed_mph, 1)} mph")

