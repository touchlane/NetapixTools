from __future__ import division
import skimage.io as io
import os
import sys
import struct
import glob


def make_output_file_url(jpg_file_url):
    output_file_name = os.path.basename(jpg_file_url).split('.')[0]
    output_file_url = os.getcwd() + '/'
    if not os.path.exists(output_file_url + "output"):
        os.makedirs(output_file_url + "output")
    return output_file_url + "output/" + output_file_name + ".npi"


def make_output_file(jpg_filepath, output_file):
    image = io.imread(jpg_filepath)
    f = open(output_file, "wb+")
    is_gray = 0
    result = []
    if len(image.shape) < 3:
        is_gray = 1
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if not is_gray:
                r, g, b = tuple(image[i][j])
                result.extend([r / 255, g / 255, b / 255])
            else:
                gray = image[i][j]
                result.append(gray / 255)
    del image
    f.write(struct.pack('%sf' % len(result), *result))
    del result
    f.close()


def jpg_to_npi_file(my_output_folder):
    if len(sys.argv) < 2:
        print("Enter path to log file")
        sys.exit()
    if ".jpg" in os.path.basename(sys.argv[1]):
        my_output_file = my_output_folder + '/' + sys.argv[1].split('/')[-1].split('.')[0] + '.npi'
        make_output_file(os.path.abspath(sys.argv[1]), my_output_file)
    else:
        print ("Wrong jpg file!")
        sys.exit()


def jpg_to_npi_folder(my_output_folder):
    if len(sys.argv) < 2:
        print("Enter path to log folder")
        sys.exit()
    first_files = glob.glob(sys.argv[1] + '/*.jpg')
    for my_filename in first_files:
        buf = my_filename.split('/')[-1].split('.')[0]
        output_file = my_output_folder + '/' + buf + ".npi"
        make_output_file(my_filename, output_file)


if __name__ == '__main__':
    output_folder = os.getcwd() + "/output"
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)
    if os.path.isfile(os.path.abspath(sys.argv[1])):
        jpg_to_npi_file(output_folder)
    else:
        jpg_to_npi_folder(output_folder)
