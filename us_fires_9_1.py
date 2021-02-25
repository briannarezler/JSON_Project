# Use the files below to compare the fires that have been burning in California between
# Sept 1-13 and Sept 14 - 20. This file contains information about the latitude and longitude,
# and the brightness of each fire. Using what you have learnt in processing a JSON files
# and mapping, make a map that shows the fires. You will need separate programs to represent
# each JSON file. One file is from 9-1-20 to 9-13-20 and the other is from 9-14-20 to 9-20-20.
#  We are only interested in fires that have a brightness factor above 450.

import json

infile = open("US_fires_9_1.json", "r")
fire_data = json.load(infile)

list_of_fires = fire_data[0:]

dates, brightnesses, lats, lons = [], [], [], []

for fire in list_of_fires:
    if fire["brightness"] >= 450:
        brightness = fire["brightness"]
        date = fire["acq_date"]
        lat = fire["latitude"]
        lon = fire["longitude"]
        brightnesses.append(brightness)
        dates.append(date)
        lats.append(lat)
        lons.append(lon)

print(brightnesses[:10])
print(dates[:10])
print(lats[:10])
print(lons[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [brightness / 30 for brightness in brightnesses],
            "color": brightnesses,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="US Fires - 9/1/2020 through 9/13/2020")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="us_fires.html")
