from __future__ import division
import os
import sys


def make_output_file_url(npo_file_url):
    output_file_name = os.path.basename(npo_file_url).split('.')[0]
    output_file_url = os.getcwd() + '/'
    if not os.path.exists(output_file_url + "output"):
        os.makedirs(output_file_url + "output")
    return output_file_url + "output/" + output_file_name + ".png"


def make_output_file(npo_filepath):
    output_file_url = make_output_file_url(npo_filepath)
    f = open(output_file_url, "w+")
    with open(npo_filepath) as file:
        for line in file:
            for num in line:
                f.write(''.join(' {}'.format(round(float(num * 255)))))


def npo_to_png_file():
    if len(sys.argv) < 2:
        print("Enter path to log file")
        sys.exit()
    if ".npo" in os.path.basename(sys.argv[1]):
        make_output_file(os.path.abspath(sys.argv[1]))
    else:
        print("Wrong .npo file! Please, check extension.")
        sys.exit()


def npo_to_png_folder():
    if len(sys.argv) < 2:
        print("Enter path to log folder")
        sys.exit()
    for subdir, dirs, files in os.walk(sys.argv[1]):
        for my_file in files:
            my_file = os.path.abspath(my_file).split(my_file)[0] + sys.argv[1] + "/" + my_file
            make_output_file(os.path.abspath(my_file))


if __name__ == '__main__':
    if os.path.isfile(os.path.abspath(sys.argv[1])):
        npo_to_png_file()
    else:
        npo_to_png_folder()
