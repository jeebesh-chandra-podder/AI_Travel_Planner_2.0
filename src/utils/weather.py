import requests
from src.config.config import WEATHER_API_KEY
from src.utils.logger import get_logger

logger = get_logger(__name__)

def get_weather(city: str) -> dict:
    """
    Fetches weather data for a given city using the WeatherAPI.
    """
    if not WEATHER_API_KEY:
        logger.warning("Weather API key is not configured. Skipping weather fetch.")
        return None

    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        weather_data = response.json()

        # Extract relevant information
        current_weather = weather_data.get("current", {})
        condition = current_weather.get("condition", {}).get("text")
        temp_c = current_weather.get("temp_c")
        wind_kph = current_weather.get("wind_kph")

        if condition and temp_c is not None:
            logger.info(f"Successfully fetched weather for {city}: {temp_c}°C, {condition}")
            return {
                "condition": condition,
                "temperature_celsius": temp_c,
                "wind_kph": wind_kph
            }
        else:
            logger.warning(f"Could not parse weather data for {city}")
            return None

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching weather for {city}: {e}")
        return None
    except Exception as e:
        logger.error(f"An unexpected error occurred while fetching weather for {city}: {e}")
        return None
