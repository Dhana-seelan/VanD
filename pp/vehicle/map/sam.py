import folium

# create a map object
mapObj = folium.Map(location=[10.8211663, 78.2897649],
                    zoom_start=5)

# add a marker object to the map
folium.Marker(location=[10.8211663, 78.2897649]
              ).add_to(mapObj)

# save the map to a html file
mapObj.save('output.html')