# import pandas lib as pd
import pandas as pd
from geopy.geocoders import Nominatim
 
def lat_lon(loc):

    #making an instance of Nominatim class
    geolocator = Nominatim(user_agent="my_request")
    
    #applying geocode method to get the location
    location = geolocator.geocode(loc)
    
    return location

# only read specific columns from an excel file
loc_df = pd.read_excel('private_school_contact_list_feb_2022-en.xlsx', usecols = [0, 6] , sheet_name = "Private Schools in Ontario")
lat = []
lon = []
for i in range(len(loc_df)):
    loc = lat_lon(loc_df.iloc[i, 1]) 
    lat.append(loc.latitude)
    lon.append(loc.longitude)
loc_df.assign(latitude = lat)
loc_df.assign(longitude = lon)
print(loc_df)