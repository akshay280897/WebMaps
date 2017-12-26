import folium
import pandas
#Creating basic map
map = folium.Map(location = [38.58,-99.09],zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup("Mygrp")
#Reading data from text file
data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data['LAT'])
lon = list(data['LON'])
#Adding Multiple Coordinate to the maps
for lt,lo in zip(lat,lon):
    fg.add_child(folium.Marker(location = [lt,lo] , popup =  "my location" , icon = folium.Icon(color = "green")))

map.add_child(fg)
map.save("map.html")
