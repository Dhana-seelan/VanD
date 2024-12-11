import folium
mapObj = folium.Map()
mapObj = folium.Map(zoom_start=5,location=[10.0731315,78.78015440000001],
                    tiles='OpenStreetMap.Mapnik')
folium.TileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',
                 name='OpenStreetMap.Mapnik',attr="OpenStreetMap.Mapnik").add_to(mapObj)
folium.TileLayer('https://tileserver.memomaps.de/tilegen/{z}/{x}/{y}.png',
                 name='OPNVKarte',attr="OPNVKarte").add_to(mapObj)
folium.TileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
                 name='OpenTopoMap',attr="OpenTopoMap").add_to(mapObj)
folium.LayerControl().add_to(mapObj)

folium.Marker(location=[10.0731315,78.78015440000001]
              ).add_to(mapObj)

mapObj.save('./folium_intro.html')
