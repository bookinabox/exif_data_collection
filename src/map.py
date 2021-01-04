import os

class Map:

    @classmethod
    def get_map(cls, coorindates):
        long, lat = coorindates[0], coordinates[1]
        os.system("start \"\" google.com/maps/@{long},{lat}", new=0, autoraise=True)