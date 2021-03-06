from PIL import Image
from PIL.ExifTags import GPSTAGS
from PIL.ExifTags import TAGS
import glob, os


def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()


def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == "GPSInfo":
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging


def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags["GPSLatitude"], geotags["GPSLatitudeRef"])

    lon = get_decimal_from_dms(geotags["GPSLongitude"], geotags["GPSLongitudeRef"])

    return (lat, lon)


def get_decimal_from_dms(dms, ref):
    degrees = dms[0]
    minutes = dms[1] / 60.0
    seconds = dms[2] / 3600.0

    if ref in ["S", "W"]:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)


def get_longitude_latitude(path):
    try:
        exif = get_exif(path)
        geotags = get_geotagging(exif)
        coord = get_coordinates(geotags)
        return coord

    except ValueError as e:
        print(e)
        return None


image_dir = "./images/*.jpg"

for file in glob.glob(image_dir):
    coord = get_longitude_latitude(file)
    print(file, coord)

if __name__ == "__main__":
    pass
