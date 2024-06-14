import requests
from datetime import datetime
import time

MY_LAT = 41.710692
MY_LONG = 44.773295

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    iss_position = (iss_longitude,iss_latitude)

    if  MY_LAT-5 <= iss_latitude <= MY_LAT and MY_LONG-5 <= iss_longitude <=MY_LONG:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Asia/Tbilisi"
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60000)
    if is_iss_overhead() and is_night():
        print("ISS is passing your location!")




