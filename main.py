from __future__ import division
import skimage.io as io
import os
import sys
import struct
import glob


def make_output_file(jpg_filepath, txt_filepath, output_file):
    if os.path.isfile(txt_filepath):
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
        with open(txt_filepath) as  my_file:
            for line in my_file:
                for num in line.strip().split(' '):
                    result.append(float(num))
        my_file.close()
        f.write(struct.pack('%sf' % len(result), *result))
        del result
        f.close()


def jpg_and_txt_to_npt_file(output):
    if len(sys.argv) < 3:
        print("Enter paths to log files")
        sys.exit()

    if ".jpg" in os.path.basename(sys.argv[1]):
        input_jpg_filepath = os.path.abspath(sys.argv[1])
        if ".txt" in os.path.basename(sys.argv[2]):
            input_txt_filepath = os.path.abspath(sys.argv[2])
        else:
            print ("Wrong txt file!")
            sys.exit()
    elif ".jpg" in os.path.basename(sys.argv[2]):
        input_jpg_filepath = os.path.abspath(sys.argv[2])
        if ".txt" in os.path.basename(sys.argv[1]):
            input_txt_filepath = os.path.abspath(sys.argv[1])
        else:
            print("Wrong txt file!")
            sys.exit()
    else:
        print ("Wrong jpg file!")
        sys.exit()
    make_output_file(input_jpg_filepath, input_txt_filepath, output)


def jpg_and_txt_to_npt_folder(my_output_folder):
    if len(sys.argv) < 3:
        print("Enter paths to log folders")
        sys.exit()
    second_path = os.path.abspath(sys.argv[2]) + '/'
    first_files = glob.glob(sys.argv[1] + '/*.jpg')
    for my_filename1 in first_files:
        buf = my_filename1.split('/')[-1].split('.')[0]
        my_filename2 = second_path + buf + ".txt"
        output_file = my_output_folder + '/' + buf + ".npt"
        make_output_file(my_filename1, my_filename2, output_file) if (".jpg" in my_filename1) else make_output_file(my_filename2, my_filename1, output_file)
        del buf
        del my_filename2


if __name__ == '__main__':
    output_folder = os.getcwd() + "/output"
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)
    if os.path.isfile(os.path.abspath(sys.argv[1])) and os.path.isfile(os.path.abspath(sys.argv[2])):
        jpg_and_txt_to_npt_file(output_folder)
    else:
        jpg_and_txt_to_npt_folder(output_folder)
