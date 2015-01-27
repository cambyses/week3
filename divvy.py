# Divvy Bikes

def main():

    import json
    import math
    from urllib.request import urlopen

    webservice_url = "http://www.divvybikes.com/stations/json"
    data = urlopen(webservice_url).read().decode("utf8")
    result = json.loads(data)
    stations = result['stationBeanList']

    count = 0
    dist_min = 100000000000
    x1 = 41.793414
    y1 = -87.600915

    #stores the closest city after each iteration.
    station_number = 0 
    for i in stations:
            x2 = result['stationBeanList'][count]['latitude']
            y2 = result['stationBeanList'][count]['longitude']
            dist = math.pow((x1-x2), 2) + math.pow((y1-y2), 2)
            if dist < dist_min and dist!= 0:
                dist_min = dist
                station_number = count
                count = count + 1
                
    #print results 'stationBeanList' and 'stationName'
    print("The nearest station is: ",result['stationBeanList'][station_number]['stationName'])
    print("There are",result['stationBeanList'][station_number]['availableBikes'],"bikes currently avaiable.")

main()


