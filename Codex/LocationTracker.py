import requests
import folium

res = requests.get("https://ipinfo.io/")
data = res.json()

location = data['loc'].split()
lat = float(location[0])
log = float(location[1])

fg = folium.FeatureGroup("my map")
fg.add_child(folium.GeoJson(data=(open('india_states.json', 'r', encoding='utf-8-sig').read())))

fg.add_child(folium.Marker(Location=[lat, log], popup="this is my location"))

map = folium.Map(Location=[lat, log], zoom_start=7)

map.add_child(fg)
map.save("index.html")
