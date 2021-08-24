#pip install folium
import folium
#dir(folium)
import pandas
data = pandas.read_csv('C:\\Users\\sachin-windows\\Heloworld\\files\\Volcanoes.txt')


lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>Height: %s m """

map = folium.Map(location=[38.58,-99.09],zoom_start=6)

fg = folium.FeatureGroup(name="My Map")

for lt, ln ,el in zip(lat, lon , elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el), icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Mapl.html")



