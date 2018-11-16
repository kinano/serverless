import os,sys
import shutil
from PIL import Image, ExifTags
import glob
from . import s3
import logging
logging.basicConfig()
logger = logging.getLogger('logger')

def handle_image(bucket, object_key):
    """
    @param bucket {}
    @param object_key str
    """
    thumbnail_width = 400
    local_file_name = '/tmp/' + object_key
    s3.download(
        key=object_key,
        bucket=bucket,
        local_file_name=local_file_name
    )
    img = Image.open(local_file_name)
    img = transpose_image(img)
    width, height = img.size
    ratio = thumbnail_width / width
    new_height = height * ratio
    size = thumbnail_width, new_height

    img.thumbnail(size)
    new_file_path = "/tmp/" + object_key
    img.save(new_file_path)
    s3.upload(
        key="thumbnails/{}".format(object_key),
        bucket=bucket,
        local_file_name=new_file_path
    )

def transpose_image(img):
    """
    Transposes the passed image to make sure it has the
    correct exif orientation
    @param img
    @returns img
    """
    if hasattr(img, "_getexif"):
        for orientation in ExifTags.TAGS.keys() :
            if ExifTags.TAGS[orientation] == "Orientation":
                break
        e = img._getexif()
        if e:
            exif = dict(e.items())
            orientation = exif.get(orientation, -1)
            if orientation == 3:
                return img.transpose(Image.ROTATE_180)
            if orientation == 6:
                return img.transpose(Image.ROTATE_270)
            if orientation == 8:
                return img.transpose(Image.ROTATE_90)
    return img