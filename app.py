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
from math import radians, cos, sin, asin, sqrt

app = Flask(__name__)
app.secret_key = 'ItShouldBeAnythingButSecret'

@app.route('/', methods = ['POST', 'GET'])
def get_values():   
        return render_template("index.html")    
 
@app.route('/result', methods = ['POST', 'GET'])
def distance_calculator():

        if(request.method == 'POST'):
            Latitude = request.form.get('Latitude')
            Longitude = request.form.get('Longitude')

        #Reading datas from CSV and import as Dataframe 
        loc_df = pd.read_csv('sample.csv') 
        
        #Stores the distances in list
        distances_km = []
        for row in loc_df.itertuples(index=False):
            distances_km.append(haversine(Latitude, Longitude, row[2], row[3]))
        
        #Adding the distances as new column to the dataframe
        loc_df['Distance']= distances_km

        #Printing the Dataframe in result.html
        return render_template('result.html',  tables=[loc_df.to_html(classes='data')], titles=loc_df.columns.values)

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

if __name__ == "__main__":
     app.run(debug=True)
