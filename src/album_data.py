import pandas as pd
import os

from map_plot import Map
from exif_extractor import ExifExtractor

from numpy import cos, sin, arcsin, sqrt
from math import radians

class ImageAlbum:

    def __init__(self, path: str):
        self.path = path
        coordinate_list = []
        for filename in os.listdir(self.path):
            if(filename.endswith(".jpg") or filename.endswith(".png")):

                exif = ExifExtractor.exif_extractor(os.path.join(self.path, filename))
                coordinates = ExifExtractor.decimal_coordinates(ExifExtractor.coordinate_extractor(exif))

                coordinate_list.append((filename, coordinates[0], -coordinates[1]))
            else:
                continue
        self.images_df = pd.DataFrame(coordinate_list, columns=['Image', 'Longitude', 'Latitude'])

    
    def distances_from_point(self, coordinate):
        self.images_df["distance"] = self.haversine((self.images_df["Longitude"],self.images_df["Latitude"]), coordinate)

    def get_image_data(self):
        return self.images_df

    def haversine(self, coord1, coord2):
        lon1 = coord2[0]
        lat1 = coord2[1]
        lon2 = coord1[0]
        lat2 = coord1[1]
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * arcsin(sqrt(a)) 
        km = 6367 * c
        return km