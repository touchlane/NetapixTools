from __future__ import division
import imageio
import os
import sys
import struct


def make_output_file_url(jpg_file_url):
    output_file_name = os.path.basename(jpg_file_url).split('.')[0]
    output_file_url = os.getcwd() + '/'
    if not os.path.exists(output_file_url + "output"):
        os.makedirs(output_file_url + "output")
    return output_file_url + "output/" + output_file_name + ".npi"


def make_output_file(jpg_filepath):
    image = imageio.imread(jpg_filepath)
    output_file_url = make_output_file_url(jpg_filepath)
    f = open(output_file_url, "w+")
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
    f.write(struct.pack('%sf' % len(result), *result))
    f.close()


def jpg_to_npi_file():
    if len(sys.argv) < 2:
        print("Enter path to log file")
        sys.exit()
    if ".jpg" in os.path.basename(sys.argv[1]):
        make_output_file(os.path.abspath(sys.argv[1]))
    else:
        print ("Wrong jpg file!")
        sys.exit()


def jpg_to_npi_folder():
    if len(sys.argv) < 2:
        print("Enter path to log folder")
        sys.exit()
    for subdir, dirs, files in os.walk(sys.argv[1]):
        for my_filename in files:
                my_filename = os.path.abspath(my_filename).split(my_filename)[0] + sys.argv[1] + "/" + my_filename
                make_output_file(os.path.abspath(my_filename))


if __name__ == '__main__':
    if os.path.isfile(os.path.abspath(sys.argv[1])):
        jpg_to_npi_file()
    else:
        jpg_to_npi_folder()
