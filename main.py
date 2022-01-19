import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "cf348c19923690dbd343239d75fb8d4a"
LAT = 5.14
LONG = 147.55

weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

will_rain = False

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_hour_data = weather_data["hourly"]
weather_data_12hour = weather_hour_data[:12]


for hour_data in weather_data_12hour:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")

