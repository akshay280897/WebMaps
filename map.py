import folium
#Creating basic map
map = folium.Map(location = [16.69,74.23],zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup("Mygrp")

#Adding Multiple Coordinate to the maps
for coordinates in [[16.5,74,2],[16.3,74.5]]:
    fg.add_child(folium.Marker(location = coordinates , popup =  "my location" , icon = folium.Icon(color = "green")))

map.add_child(fg)
map.save("map.html")
