from PIL import Image
from fractions import Fraction

class ExifExtractor:
    
    def __init__(self):
        pass
    @staticmethod
    def exif_extractor(path):
       img = Image.open(path)
       return img._getexif() 
    
    @classmethod
    def coordinate_extractor(cls, exif):
        gps_data = exif[34853]
        coordinates = (gps_data[2], gps_data[4])
        return (coordinates[0],coordinates[1])
    
    @classmethod
    def DMS_to_decimal(cls, coordinate):
        
        return Fraction.__float__(coordinate[0] + coordinate[1]/60 + coordinate[2]/3600)

    @classmethod
    def decimal_coordinates(cls, coordinates):
        return (cls.DMS_to_decimal(coordinates[0]), cls.DMS_to_decimal(coordinates[1]))