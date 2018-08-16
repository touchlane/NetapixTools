from __future__ import division
import os
import sys
import numpy as np
import glob


def make_output_file(npo_filepath, output_file):
    f = open(output_file, "w+")
    with open(npo_filepath, 'rb') as file:
        array = np.fromfile(file, dtype=np.float32)
        print(array)
        array = map(lambda x: round(x, 7), array)
        print(array)
        np.savetxt(f, array, newline=' ', fmt='%.7f')


def npo_to_txt_file(my_output_folder):
    if len(sys.argv) < 2:
        print("Enter path to log file")
        sys.exit()
    if ".npo" in os.path.basename(sys.argv[1]):
        my_output_file = my_output_folder + '/' + sys.argv[1].split('/')[-1].split('.')[0] + '.txt'
        make_output_file(os.path.abspath(sys.argv[1]), my_output_file)
    else:
        print("Wrong .npo file! Please, check extension.")
        sys.exit()


def npo_to_txt_folder(output_folder):
    if len(sys.argv) < 2:
        print("Enter path to log folder")
        sys.exit()
    files = glob.glob(sys.argv[1] + '/*.npo')
    for my_file in files:
        buf = my_file.split('/')[-1].split('.')[0]
        output_file = output_folder + '/' + buf + '.txt'
        make_output_file(my_file, output_file)


if __name__ == '__main__':
    output_folder = os.getcwd() + "/output"
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)
    if os.path.isfile(os.path.abspath(sys.argv[1])):
        npo_to_txt_file(output_folder)
    else:
        npo_to_txt_folder(output_folder)
