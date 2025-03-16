import datetime
import openmeteo_requests
import requests_cache
from retry_requests import retry

import requests

def fetch_weather(latitude, longitude):
    """
    Fetches weather data from Open-Meteo API based on latitude and longitude.
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weather_code,temperature_2m_max,temperature_2m_min,sunshine_duration,rain_sum,snowfall_sum&timezone=auto&forecast_days=14"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses (4xx and 5xx)
        data = response.json()

        # Construct structured dictionary
        daily_data = []
        for i in range(len(data["daily"]["time"])):
            daily_data.append({
                "date": data["daily"]["time"][i],
                "weather_code": data["daily"]["weather_code"][i],
                "temperature_2m_max": data["daily"]["temperature_2m_max"][i],
                "temperature_2m_min": data["daily"]["temperature_2m_min"][i],
                "sunshine_duration": data["daily"]["sunshine_duration"][i],
                "rain_sum": data["daily"]["rain_sum"][i],
                "snowfall_sum": data["daily"]["snowfall_sum"][i]
            })

        return daily_data
    except requests.RequestException:
        return {"error": "Weather data unavailable"}
    

## KNOWN BUG using the open meteo client does not work

'''
# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)


def fetch_weather_forecast(latitude, longitude):
    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunshine_duration", "rain_sum", "snowfall_sum"],
        "timezone": "auto",
        "forecast_days": 14
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation {response.Elevation()} m asl")
    print(f"Timezone {response.Timezone()}{response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Extract daily weather data
    daily = response.Daily()
    daily_weather_code = daily.Variables(0).ValuesAsNumpy().tolist()
    daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy().tolist()
    daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy().tolist()
    daily_sunshine_duration = daily.Variables(3).ValuesAsNumpy().tolist()
    daily_rain_sum = daily.Variables(4).ValuesAsNumpy().tolist()
    daily_snowfall_sum = daily.Variables(5).ValuesAsNumpy().tolist()

    # Convert timestamps to readable dates
    start_time = datetime.utcfromtimestamp(daily.Time())
    end_time = datetime.utcfromtimestamp(daily.TimeEnd())
    interval = datetime.timedelta(seconds=daily.Interval())

    # Generate date range
    dates = []
    current_time = start_time
    while current_time < end_time:
        dates.append(current_time.strftime("%Y-%m-%d"))
        current_time += interval

    # Construct structured dictionary
    daily_data = []
    for i in range(len(dates)):
        daily_data.append({
            "date": dates[i],
            "weather_code": daily_weather_code[i],
            "temperature_2m_max": daily_temperature_2m_max[i],
            "temperature_2m_min": daily_temperature_2m_min[i],
            "sunshine_duration": daily_sunshine_duration[i],
            "rain_sum": daily_rain_sum[i],
            "snowfall_sum": daily_snowfall_sum[i]
        })

    # Print structured daily forecast
    for entry in daily_data:
        print(entry)

    return daily_data
    '''