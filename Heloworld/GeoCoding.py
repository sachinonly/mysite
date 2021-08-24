#Bug in Python
# from geopy.geocoders import Nominatim
# nom = Nominatim()
# change them to these
#
# from geopy.geocoders import ArcGIS
# nom = ArcGIS()

#pip install geopy
import os
import pandas
# os.listdir()
from geopy.geocoders import ArcGIS
nom = ArcGIS()

df1 = pandas.read_csv("C:\\Users\\sachin-windows\\Heloworld\\files\\supermarkets\\supermarkets.csv")
df1["Address"] = df1["Address"]+", "+ df1["City"]+ ", "+ df1["Country"]
df1["Coordinates"]=df1["Address"].apply(nom.geocode)
#df1.Coorindates
#df1.Coordinates[0].latitude
df1["Latitude"]=df1["Coordinates"].apply(lambda x : x.latitude if x != None else None)
df1["Longitude"]=df1["Coordinates"].apply(lambda x : x.longitude if x != None else None)
print (df1)