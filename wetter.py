from requests import get
import json
import folium
import os
import webbrowser
import html
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
stations = get(url).json()
print(stations['items'][0])

lons = [station['weather_stn_long'] for station in stations['items']]
lats = [station['weather_stn_lat'] for station in stations['items']]
wsnames = [html.escape(station['weather_stn_name']) for station in stations['items']]

map_ws = folium.Map(location=[0,0],zoom_start=2)
CWD = os.getcwd()
for n in range(len(lons)):
    folium.Marker([lats[n],
                lons[n]],
                icon = folium.Icon(icon = 'heart', color = 'red'),
                popup = wsnames[n]).add_to(map_ws)
map_ws.save('wsmap1.html')
webbrowser.open_new('file://'+CWD+'/'+'wsmap1.html')

