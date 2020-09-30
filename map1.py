import folium

map = folium.Map(location = [28.6139,77.2090], zoom_start=6, tiles='Stamen Terrain')

fg = folium.FutureGroup(name="My Map")
fg.add_child(folium.Marker(location=[28.6,77.2], popup="I am Marker", icon=folium.Icon(color="red")))
map.add_child(fg)

map.save("Map1.html")
