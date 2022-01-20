import requests
import os
from twilio.rest import Client
import smtplib

# openweather parameter
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "cf348c19923690dbd343239d75fb8d4a"
# LAT = 30.996893
# LONG = 103.620529
LAT = 5.14
LONG = 147.55
weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

# twilio parameter
account_sid = "AC8a95a85cabd382f190b3ac17e0a97d26"
auth_token = "1c531beaff38baf0e0b5b5148a225b61"

# email parameter
EMAIL = "562937707@qq.com"
PASSWORD = "bpyjiqjylklcbdhe"


def send_email():
    with smtplib.SMTP("smtp.qq.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject:Today Will Rain!\n\nTake the umbrella."
                            )
        print("Email sent.")


def get_weather_slice():
    response = requests.get(OWM_ENDPOINT, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()
    weather_hour_data = weather_data["hourly"]
    weather_12_hours = weather_hour_data[:12]
    return weather_12_hours


def send_sms():
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It will rain today,take your umbrella.今天会下雨，记得带伞。☔",
            from_="+16065540848",
            to="+8619808145773"
        )
    print(message.status)


weather_slice = get_weather_slice()

will_rain = False
for hour_data in weather_slice:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("sent")
    send_sms()
    send_email()
