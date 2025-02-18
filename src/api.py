import os
import requests
from dotenv import load_dotenv
from typing import Tuple, Dict, Any, Optional

load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("Missing API key. Set it in an .env file under API_KEY.")

BASE_URL = f"https://api.openweathermap.org/data/2.5/weather"


def get_weather_data(
    city: str,
) -> Tuple[Optional[Dict[str, Any]], Optional[Tuple[str, int]]]:
    """
    Fetch weather data from openweather api

    :param city: Name of city to fetch weather from
    :return: A tuple based on result from fetch
        - First value if weather data dict is successful
        - Second value is a tuple (error_message, status_code) if an error occurs, else None

    """

    url = f"{BASE_URL}?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTP errors to exception
        data = response.json()

        # Success state
        if data["cod"] == 200:
            return data, None

    # Fail state
    except requests.exceptions.HTTPError as http_error:
        match response.status_code:
            case 400:
                return ("Bad request:\nPlease check your input", 400)
            case 401:
                return ("Unauthorized:\nInvalidate API key", 401)
            case 403:
                return ("Access denied:\nAccess is denied", 403)
            case 404:
                return ("Not found:\nCity not found", 404)
            case 500:
                return ("Internal server error:\nPlease try again later", 500)
            case 502:
                return ("Bad gateway:\nInvalid response from the server", 502)
            case 503:
                return ("Service Unavailable:\nServer is down", 503)
            case 504:
                return ("Gateway timeout:\nNo response from the server", 504)
            case _:
                return (f"HTTP error occured\n{http_error}", response.status_code)
    except requests.exceptions.ConnectionError:
        return ("Connection Error:\n Check your internet connection", 0)
    except requests.exceptions.Timeout:
        return ("Timeout Error:\nThe request timed out", 0)
    except requests.exceptions.TooManyRedirects:
        return ("Too many redirects:\nCheck the URL", 0)
    except requests.exceptions.RequestException as req_error:
        return (f"Request Error:\n{req_error}", 0)
    return None, None  # Unexpected scenario NOTHING happens.
