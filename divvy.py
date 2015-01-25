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
