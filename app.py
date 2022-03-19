'''
Created on 
Course work: 
@author: Saaisri , Sivaraam
Source:
    
'''

# Source : https://towardsdatascience.com/heres-how-to-calculate-distance-between-2-geolocations-in-python-93ecab5bbba4

# Find the set of schools near a given location

from flask import  Flask,render_template, request
from flask import *
from math import radians
import pandas as pd
import numpy as np
import csv
from math import radians, cos, sin, asin, sqrt


# app = Flask(__name__)


# @app.route('/',methods = ['GET','POST'])

#     return render_template('index.html',posts = distances_km)



app = Flask(__name__)
app.secret_key = 'ItShouldBeAnythingButSecret'



@app.route('/', methods = ['POST', 'GET'])
def get_values():
    
    return render_template("index.html")    
 
@app.route('/result', methods = ['POST', 'GET'])
def distance_calculator():

    # Latitude=12.6546315
    # Longitude=45.15651

    if(request.method == 'POST'):
        Latitude = request.form.get('Latitude')
        Longitude = request.form.get('Longitude') 

        cities = pd.DataFrame(data={
            'City': ['Osahwa', 'Miami', 'Chicago'],
            'Lat' : [43.875081898250606, 25.7825453, 41.8339037],
            'Lon' : [-78.85530108422006, -80.2994985, -87.8720471]
        })

        distances_km = []
        for row in cities.itertuples(index=False):
                distances_km.append(haversine(Latitude, Longitude, row.Lat, row.Lon))
        
        return render_template("result.html",dist = distances_km)

def haversine(lon1, lat1, lon2, lat2):

        lon1 = float(lon1)
        lat1 = float(lat1)
        lon2 = float(lon2)
        lat2 = float(lat2)
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
        r = 6371 
        # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
        return c * r

# cities_df = pd.read_csv('landmark.csv')

# 43.90326739297604, -78.87011798647485

        

# cities_df['lat'] = np.radians(cities_df['lat'])
# cities_df['lon'] = np.radians(cities_df['lon'])

# cities_df.head()

    
    
    # cities['DistanceFromNY'] = distances_km
    
    
    # return "<h3>Current location entered</h3>"   


if __name__ == "__main__":
     app.run(debug=True)

























# from flask import Flask, render_template, request, redirect, url_for
# app = Flask(__name__)

# @app.route('/')
# def index():

#     return render_template("index.html")

# @app.route('/result',methods=['GET'])

# # start_lat, start_lon = 12.94315265341667, 80.14169879797205


# def result():



# if __name__ == '__main__':
#     app.run(debug = True)