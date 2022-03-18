import numpy as np
import pandas as pd
from math import radians, cos, sin, asin, acos, sqrt, pi
from geopy import distance
from geopy.geocoders import Nominatim
import osmnx as ox
import networkx as nx
lat1, lon1 = -37.82120, 144.96441 # location 1
lat2, lon2 = -37.88465,  145.08727 # location 2

def calculate_spherical_distance(lat1, lon1, lat2, lon2, r=6371):
    # Convert degrees to radians
    coordinates = lat1, lon1, lat2, lon2
    # radians(c) is same as c*pi/180
    phi1, lambda1, phi2, lambda2 = [
        radians(c) for c in coordinates
    ]  
    
    # Apply the haversine formula
    a = (np.square(sin((phi2-phi1)/2)) + cos(phi1) * cos(phi2) * 
         np.square(sin((lambda2-lambda1)/2)))
    d = 2*r*asin(np.sqrt(a))
    return d
print(f"{calculate_spherical_distance(lat1, lon1, lat2, lon2):.4f} km")

def calculate_spherical_distance(lat1, lon1, lat2, lon2, r=6371):
    # Convert degrees to radians
    coordinates = lat1, lon1, lat2, lon2
    phi1, lambda1, phi2, lambda2 = [
        radians(c) for c in coordinates
    ]
    
    # Apply the haversine formula
    d = r*acos(cos(phi2-phi1) - cos(phi1) * cos(phi2) *
              (1-cos(lambda2-lambda1)))
    return d

print(f"{calculate_spherical_distance(lat1, lon1, lat2, lon2):.4f} km")

print(f"{distance.great_circle((lat1, lon1), (lat2, lon2)).km:.4f} km")

mel_graph = ox.graph_from_place(
    'Melbourne, Australia', network_type='drive', simplify=True
)
ox.plot_graph(mel_graph)

orig_node = ox.distance.nearest_nodes(mel_graph, lon1, lat1)
target_node = ox.distance.nearest_nodes(mel_graph, lon2, lat2)
nx.shortest_path_length(G=mel_graph, source=orig_node, target=target_node, weight='length')

def calculate_driving_distance(lat1, lon1, lat2, lon2):
    # Get city and country name
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(f"{lat1}, {lon1}")
    address = location.raw['address']
    area = f"{address['city']}, {address['country']}"
    # Get graph for the city
    graph = ox.graph_from_place(area, network_type='drive', 
                                simplify=True)
    # Find shortest driving distance
    orig_node = ox.distance.nearest_nodes(graph, lon1, lat1)
    target_node = ox.distance.nearest_nodes(graph, lon2, lat2)
    length = nx.shortest_path_length(G=graph, source=orig_node, 
                                     target=target_node, weight='length')
    return length / 1000 # convert from m to kms
print(f"{calculate_driving_distance(lat1, lon1, lat2, lon2):.2f} km")

