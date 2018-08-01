from __future__ import division
import imageio
import os
import sys


def make_output_file_url(jpg_file_url):
    output_file_name = os.path.basename(jpg_file_url).split('.')[0]
    output_file_url = os.getcwd() + '/'
    if not os.path.exists(output_file_url + "output"):
        os.makedirs(output_file_url + "output")
    return output_file_url + "output/" + output_file_name + ".npt"


def make_output_file(jpg_filepath, txt_filepath):
    image = imageio.imread(jpg_filepath)
    output_file_url = make_output_file_url(jpg_filepath)
    f = open(output_file_url, "w+")
    is_gray = 0
    result = ""
    if len(image.shape) < 3:
        is_gray = 1
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if not is_gray:
                r, g, b = tuple(image[i][j])
                result += '{} {} {} '.format(r / 255, g / 255, b / 255)
            else:
                gray = image[i][j]
                result += '{} '.format(gray / 255)
    with open(txt_filepath) as file:
        for line in file:
            for num in line:
                result += ' {}'.format(num)
    f.write(result)


def jpg_and_txt_to_npt_file():
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
    make_output_file(input_jpg_filepath, input_txt_filepath)


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
                        make_output_file(os.path.abspath(my_filename1), os.path.abspath(my_filename2)) if (".jpg" in my_filename1) else make_output_file(os.path.abspath(my_filename2), os.path.abspath(my_filename1))


if __name__ == '__main__':
    print (os.getcwd())
    if os.path.isfile(os.path.abspath(sys.argv[1])) and os.path.isfile(os.path.abspath(sys.argv[2])):
        jpg_and_txt_to_npt_file()
    else:
        jpg_and_txt_to_npt_folder()
