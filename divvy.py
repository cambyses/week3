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

count = 0
x1 = 41.793414
y1 = -87.600915

#stores the closest city after each iteration.
station_number = 0 

