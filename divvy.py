# Divvy Bikes
#
# Here's an example of how to retrieve the list of Divvy bike stations:

import math
import json
from urllib.request import urlopen

webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)
stations = result['stationBeanList']
print(stations)

# row number at initioation
row_number = 0

# Young location
x1 = 41.793414
y1 = -87.600915

#storing the closest station after each iteration.
station_number = 0
for i in stations:
    x2 = result['stationBeanList'][row_number]['latitude']
    y2 = result['stationBeanList'][row_number]['longitude']

#

station_number = row_number
row_number = row_number + 1


