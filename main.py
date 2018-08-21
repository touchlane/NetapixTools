from __future__ import division
from PIL import Image
import os
import sys
import glob
import numpy as np


def make_output_file(npo_filepath, output_file):
    buf = np.zeros([int(sys.argv[2]), int(sys.argv[3]), 4], dtype=np.uint8)
    array = np.fromfile(npo_filepath, dtype=np.float32)
    if len(array) / (int(sys.argv[2]) * int(sys.argv[3])) == 1:
        is_gray = 1
    else:
        is_gray = 0
    real_array = []
    temp = []
    if is_gray:
        [real_array.extend([[i] * 3]) for i in array]
    else:
        for i in range(0, len(array), 3):
            temp = [array[i], array[i+1], array[i+2]]
            real_array.extend([temp])
    index = 0
    for i in range(int(sys.argv[2])):
        for j in range(int(sys.argv[3])):
            real_array[index] = list(map(lambda x: x*255, real_array[index]))
            real_array[index].append(255)
            buf[i, j] = real_array[index]
            index += 1
    im = Image.fromarray(np.array(buf))
    im.save(output_file)


def npo_to_png_file(my_output_folder):
    if len(sys.argv) < 4:
        print("Wrong input! python3 main.py [path/*.npo] [width] [height]")
        sys.exit()
    if ".npo" in os.path.basename(sys.argv[1]):
        my_output_file = my_output_folder + '/' + sys.argv[1].split('/')[-1].split('.')[0] + '.png'
        make_output_file(os.path.abspath(sys.argv[1]), my_output_file)
    else:
        print("Wrong .npo file! Please, check extension.")
        sys.exit()


def npo_to_png_folder(my_output_folder):
    if len(sys.argv) < 4:
        print("Wrong input! python3 main.py [path to folder with .npo] [width] [height]")
        sys.exit()
    files = glob.glob(sys.argv[1] + '/*.npo')
    if len(files) > 0:
        for my_file in files:
            buf = my_file.split('/')[-1].split('.')[0]
            output_file = my_output_folder + '/' + buf + '.png'
            make_output_file(my_file, output_file)
    else:
        print("There is no .npo files in the given folder!")
        sys.exit()


if __name__ == '__main__':
    output_folder = os.getcwd() + "/output"
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)
    if os.path.isfile(os.path.abspath(sys.argv[1])):
        npo_to_png_file(output_folder)
    else:
        npo_to_png_folder(output_folder)
