
from math import radians
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

# cities_df = pd.read_csv('landmark.csv')

# 43.90326739297604, -78.87011798647485

cities = pd.DataFrame(data={
   'City': ['Osahwa', 'Miami', 'Chicago'],
   'Lat' : [43.875081898250606, 25.7825453, 41.8339037],
   'Lon' : [-78.85530108422006, -80.2994985, -87.8720471]
})


#toronto

start_lat, start_lon = 12.94315265341667, 80.14169879797205

distances_km = []

for row in cities.itertuples(index=False):
   distances_km.append(haversine(start_lat, start_lon, row.Lat, row.Lon))

print(distances_km)
cities['DistanceFromNY'] = distances_km

