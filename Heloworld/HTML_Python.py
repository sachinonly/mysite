#pip install folium
import folium
#dir(folium)
map = folium.Map(location=[17.504493, 78.326464],zoom_start=60)

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[17.504493, 78.326464], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Mapl.html")



