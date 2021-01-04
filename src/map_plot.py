import webbrowser
import numpy as np
from haversine import haversine, Unit

from exif_extractor import ExifExtractor
class Map:

    @staticmethod
    def get_map(coordinates):
        longitude, latitude = coordinates
        url = f"https://google.com/maps/search/?api=1&query={longitude},{-latitude}"
        print(url)
        webbrowser.open(url)

    @staticmethod
    def distance_coordinates(coord1, coord2):
        return haversine(coord1, coord2, unit='mi')