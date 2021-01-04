import os

from exif_extractor import ExifExtractor
from map_plot import Map
from album_data import ImageAlbum

if __name__ == "__main__":

    path = ""
    Signs = ImageAlbum(path)
    Signs.distances_from_point((34.1177828,-118.0674309))
    print(Signs.get_image_data())
    # Map.get_map(coordinates)