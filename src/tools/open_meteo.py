import requests

def fetch_weather(latitude: float, longitude: float):
    """
    Fetch simple weather data from Open-Meteo API.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
