from requests import get
from datetime import datetime

MY_LAT = 28.703870
MY_LONG = 77.146410

params = {
    'lat': MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = get('https://api.sunrise-sunset.org/json', params=params)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise, sunset)
