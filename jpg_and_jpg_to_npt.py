from __future__ import division
import imageio
import os
import sys


def make_output_file_url(jpg_file_url):
    output_file_name = os.path.basename(jpg_file_url).split('.')[0]
    output_file_url = jpg_file_url.split(output_file_name)[0].split(sys.argv[1])[0]
    if not os.path.exists(output_file_url + "output"):
        os.makedirs(output_file_url + "output")
    return output_file_url + "output/" + output_file_name + ".npt"


def write_jpg_to_output_file(jpg_filepath, file):
    image = imageio.imread(jpg_filepath, as_gray=False, pilmode="RGB")
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            r, g, b = tuple(image[i][j])
            file.write(''.join('{} {} {} '.format(r / 255, g / 255, b / 255)))


def make_output_file(jpg_first_filepath, jpg_second_filepath):
    output_file_url = make_output_file_url(jpg_first_filepath)
    f = open(output_file_url, "w+")
    write_jpg_to_output_file(jpg_first_filepath, f)
    write_jpg_to_output_file(jpg_second_filepath, f)


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


def jpg_and_txt_to_npt_folder():
    if len(sys.argv) < 3:
        print("Enter paths to log folders")
        sys.exit()
    for subdir, dirs, first_files in os.walk(sys.argv[1]):
        for subdir, dirs, second_files in os.walk(sys.argv[2]):
            for my_filename1 in first_files:
                for my_filename2 in second_files:
                    if my_filename1.split(".")[0] == my_filename2.split(".")[0]:
                        my_filename1 = os.path.abspath(my_filename1).split(my_filename1)[0] + sys.argv[1] + "/" + my_filename1
                        my_filename2 = os.path.abspath(my_filename2).split(my_filename2)[0] + sys.argv[2] + "/" + my_filename2
                        make_output_file(os.path.abspath(my_filename1), os.path.abspath(my_filename2))


if __name__ == '__main__':
    if os.path.isfile(os.path.abspath(sys.argv[1])) and os.path.isfile(os.path.abspath(sys.argv[2])):
        jpg_and_txt_to_npt_file()
    else:
        jpg_and_txt_to_npt_folder()
