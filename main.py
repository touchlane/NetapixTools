import os
import sys
import glob
from PIL import Image


def png_to_jpg(image_path, output_path):
    image = Image.open(image_path)
    jpg_image = image.convert("RGB")
    jpg_image.save(output_path + '/' + image_path.split("/")[-1].split(".")[0] + ".jpg")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("It is not enough arguments to work! python main.py [path/*.png]")
        sys.exit()
    output_path = os.getcwd() + "/output"
    if not os.path.isdir(output_path):
        os.makedirs(output_path)
    if os.path.isdir(sys.argv[1]):
        png_images = glob.glob(os.path.abspath(sys.argv[1]) + "/*.png")
        for png_image in png_images:
            png_to_jpg(png_image, output_path)
    else:
        png_to_jpg(os.path.abspath(sys.argv[1]), output_path)
