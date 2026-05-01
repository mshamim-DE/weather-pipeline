import requests

def fetch_weather(city, latitude, longitude):
    print(f"Fetching weather for {city}...")

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
        "hourly": ["relativehumidity_2m", "direct_radiation"]
    }

    response = requests.get(url, params=params)

    data = response.json()

    print("Raw data received!")
    print(data)

    return data

# Run it
fetch_weather("Delhi", 28.6139, 77.2090)