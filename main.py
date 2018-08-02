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
    return output_file_url + "output/" + output_file_name + ".npt"


def write_jpg_to_output_file(jpg_filepath, f):
    image = io.imread(jpg_filepath)
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
    del result


def make_output_file(jpg_first_filepath, jpg_second_filepath, output_file):
    if os.path.isfile(jpg_second_filepath):
        f = open(output_file, "wb+")
        write_jpg_to_output_file(jpg_first_filepath, f)
        write_jpg_to_output_file(jpg_second_filepath, f)
        f.close()


def jpg_and_txt_to_npt_file():
    if len(sys.argv) < 3:
        print("Enter paths to log files")
        sys.exit()

    if ".jpg" in os.path.basename(sys.argv[1]) and ".jpg" in os.path.basename(sys.argv[2]):
        input_first_jpg_filepath = os.path.abspath(sys.argv[1])
        input_second_jpg_filepath = os.path.abspath(sys.argv[2])
    else:
        print ("Something wrong with jpg filenames!")
        sys.exit()
    make_output_file(input_first_jpg_filepath, input_second_jpg_filepath)


def jpg_and_txt_to_npt_folder(output):
    if len(sys.argv) < 3:
        print("Enter paths to log folders")
        sys.exit()
    second_path = os.path.abspath(sys.argv[2]) + '/'
    first_files = glob.glob(sys.argv[1] + '/*.jpg')
    for my_filename1 in first_files:
        buf = my_filename1.split('/')[-1]
        my_filename2 = second_path + buf
        output_file = output + '/' + buf.split('.')[0] + ".npt"
        make_output_file(my_filename1, my_filename2, output_file) if (".jpg" in my_filename1) else make_output_file(my_filename2, my_filename1, output_file)
        del buf
        del my_filename2


if __name__ == '__main__':
    output_folder = os.getcwd() + "/output"
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)
    if os.path.isfile(os.path.abspath(sys.argv[1])) and os.path.isfile(os.path.abspath(sys.argv[2])):
        jpg_and_txt_to_npt_file()
    else:
        jpg_and_txt_to_npt_folder(output_folder)
