import pandas as pd
from pyproj import Transformer
import folium


def create_map_origin_destination(df,x_origin,y_origin,x_destination,y_destination,zoom,need_transform):

    if need_transform ==1:
        # ## IF NEEDS TRANSFORMATION
        transformer = Transformer.from_crs("epsg:2154", "epsg:4326")
        latlong_origin = list(zip(*transformer.transform(df[x_origin], df[y_origin])))
        latlong_destination = list(zip(*transformer.transform(df[x_destination], df[y_destination])))
        m = folium.Map(latlong_origin[0], zoom_start=zoom)
    else:
        latlong_origin = list(zip(df[x_origin], df[y_origin]))
        latlong_destination = list(zip(df[x_destination], df[y_destination]))
        m = folium.Map(latlong_origin[0], zoom_start=zoom)

    for origin, destination in zip(latlong_origin, latlong_destination):
        folium.CircleMarker([origin[0], origin[1]],
                            radius=15,
                            fill_color="#3db7e4red", # divvy color
                        ).add_to(m)

        folium.CircleMarker([destination[0], destination[1]],
                            radius=15,
                            fill_color="green", # divvy color
                        ).add_to(m)

        folium.PolyLine([[origin[0], origin[1]], 
                        [destination[0], destination[1]]]).add_to(m)
    return(m)
    

