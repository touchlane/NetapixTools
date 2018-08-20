from __future__ import division
import sys
import os
import glob
from PIL import Image
import cv2


def rotate_image(filepath, orientation, outputpath):
    image = Image.open(filepath)
    width, height = image.size
    if orientation.upper() == "PORTRAIT" and width > height:
        image = image.rotate(90, expand=True)
    elif orientation.upper() == "LANDSCAPE" and width < height:
        image = image.rotate(90, expand=True)
    image.save(outputpath + '/' + filepath.split('/')[-1], "JPEG")


def adjust_image(filepath, width, height, outputpath):
    image = cv2.imread(filepath)
    cur_height, cur_width = image.shape[:2]
    if width * height < cur_height * cur_width:
        new_dim = cur_width if cur_width - width < cur_height - height else cur_height
        new_dim_2 = new_dim * height / width if new_dim == cur_width else new_dim * width / height
        new_x = 0 if new_dim == cur_width else (cur_width - new_dim_2) / 2
        new_y = 0 if new_dim == cur_height else (cur_height - new_dim_2) / 2
        new_width = new_dim if new_dim == cur_width else new_dim_2
        new_height = new_dim if new_dim == cur_height else new_dim_2
        cropped_image = image[int(new_y): int(new_y + new_height), int(new_x): int(new_x + new_width)]
        cur_height, cur_width = cropped_image.shape[:2]
        ratio_x = width / cur_width
        ratio_y = height / cur_height
        image = cv2.resize(cropped_image, (0, 0), fx=ratio_x, fy=ratio_y)
        cv2.imwrite(outputpath + '/' + filepath.split('/')[-1], image)
        

def process_images(operation, outputpath):
    images = glob.glob(sys.argv[1] + "/*.jpg")
    if operation == "rotate":
        for image in images:
            rotate_image(image, sys.argv[2], outputpath)
    elif operation == "resize":
        for image in images:
            adjust_image(image, int(sys.argv[2]), int(sys.argv[3]), outputpath)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Some parameters missed! python3 main.py [path/*.jpg] 1) [orientation] 2)[desired_width] [desired_height]")
        sys.exit()
    if os.path.isdir(sys.argv[1]):
        outputpath = os.getcwd() + '/output'
        if not os.path.isdir(outputpath):
            os.makedirs(outputpath)
        if len(sys.argv) == 3 and (sys.argv[2].upper() == "PORTRAIT" or sys.argv[2].upper() == "LANDSCAPE"):
            process_images("rotate", outputpath)
        elif len(sys.argv) == 4:
            process_images("resize", outputpath)
    else:
        print("Wrong parameters! Check for typos in orientation parameter.")
        sys.exit()
