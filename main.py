import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "cf348c19923690dbd343239d75fb8d4a"
LAT = 30.6667
LONG = 104.0667

parameter = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY
}

response = requests.get(OWM_ENDPOINT, params=parameter)
response.raise_for_status()
data = response.json()

hourly = data["hourly"]
