from flask import  Flask,render_template, request
from flask import *
from math import radians
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt


# app = Flask(__name__)


# @app.route('/',methods = ['GET','POST'])

#     return render_template('index.html',posts = distances_km)



app = Flask(__name__)
app.secret_key = 'ItShouldBeAnythingButSecret'

Latitude1=12.6546315
Longitude1=45.15651

@app.route('/', methods = ['POST', 'GET'])
def get_values():
    if(request.method == 'POST'):
        Latitude = request.form.get('Latitude')
        Longitude = request.form.get('Longitude') 
        location['Latitude'],location['Longitude'] = Latitude, Longitude
    return render_template("index.html")    
 
@app.route('/result')
def distance_calculator():

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
        r = 6371 
        # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
        return c * r

# cities_df = pd.read_csv('landmark.csv')

# 43.90326739297604, -78.87011798647485

    cities = pd.DataFrame(data={
   'City': ['Osahwa', 'Miami', 'Chicago'],
   'Lat' : [43.875081898250606, 25.7825453, 41.8339037],
   'Lon' : [-78.85530108422006, -80.2994985, -87.8720471]
})

# cities_df['lat'] = np.radians(cities_df['lat'])
# cities_df['lon'] = np.radians(cities_df['lon'])

# cities_df.head()

    distances_km = []
    for row in cities.itertuples(index=False):
        distances_km.append(haversine(Latitude1, Longitude1, row.Lat, row.Lon))
    
    # cities['DistanceFromNY'] = distances_km
    
    return render_template("result.html",dist = distances_km)
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
