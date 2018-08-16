from __future__ import division
import sys
import os
import glob
from PIL import Image
import cv2


def crop(pil_image, outputpath, imagename):
    area = (0, 0, 3024, 3024)
    image_pil = pil_image.crop(area)
    size = (480, 480)
    image_pil.thumbnail(size, Image.ANTIALIAS)
    image_pil.save(outputpath + '/' + imagename, "JPEG")


def adjust_image(filepath, orientation, outputpath):
    imagename = filepath.split('/')[-1]
    image = cv2.imread(filepath)
    cur_height, cur_width = image.shape[:2]
    isPortrait = True if cur_height > cur_width else False
    if cur_width/cur_height == 3024/4032 or cur_width/cur_height == (3024/4032)**(-1):
        if cur_height != 4032 and cur_width != 3024:
            if isPortrait:
                ratio_x = 3024/cur_width
                ratio_y = 4032/cur_height
                image = cv2.resize(image, (0, 0), fx=ratio_x, fy=ratio_y)
            else:
                ratio_x = 4032 / cur_width
                ratio_y = 3024 / cur_height
                image = cv2.resize(image, (0, 0), fx=ratio_x, fy=ratio_y)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(image)
    if not image_pil.size[0] < image_pil.size[1]:
        image_pil = image_pil.rotate(90, expand=True)
    crop(image_pil, outputpath, imagename)


def adjust_images(orientation, outputpath):
    images = glob.glob(sys.argv[1] + "/*.jpg")
    for image in images:
        adjust_image(image, orientation, outputpath)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Some parameters missed! python3 main.py [path/*.jpg] [orientation]")
        sys.exit()
    if os.path.isdir(sys.argv[1]) and (sys.argv[2].upper() == "PORTRAIT" or sys.argv[2].upper() == "LANDSCAPE"):
        outputpath = os.getcwd() + '/output'
        if not os.path.isdir(outputpath):
            os.makedirs(outputpath)
        adjust_images(sys.argv[2].lower(), outputpath)
    else:
        print("Wrong parameters! Check for typos in orientation parameter.")
        sys.exit()
