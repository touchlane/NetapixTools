from __future__ import division
import os
import sys
import numpy as np
import glob
import skimage.io as io


def get_file_accuracy(output_file, label_file):
    with open(output_file, "rb") as o_f:
        result_array = np.fromfile(o_f, dtype=np.float32)
        o_f.close()
    with open(label_file, "rb") as l_f:
        tmp = np.loadtxt(l_f, dtype=np.float32) if ".txt" in label_file else io.imread(label_file)
        label_array = tmp.ravel()
        l_f.close()
    buf = label_array - result_array
    file_error = sum(buf ** 2 / 2)
    return file_error


def get_accuracy(output_folder, label_folder, is_txt):
    max_error = 0
    sum_error = 0
    output_files = glob.glob(os.path.abspath(sys.argv[1]) + "/*.npo")
    for output_file in output_files:
        buf = sys.argv[2] + "/" + output_file.split("/")[-1].split(".")[0]
        label_file = buf + ".txt" if is_txt else buf + ".jpg"
        error = get_file_accuracy(output_file, label_file)
        if error > max_error:
            max_error = error
        sum_error += error
    mean_error = sum_error / len(output_files)
    print("Accuracy: {}%".format((1 - mean_error/max_error) * 100))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("main.py [path/results.txt] [path/labels.txt]")
        sys.exit()
    if not (os.path.isdir(sys.argv[1]) or os.path.isdir(sys.argv[2])):
        print("Wrong input! Accuracy for only one input file will be 0.")
        sys.exit()
    else:
        if ".jpg" in os.listdir(sys.argv[2])[0]:
            get_accuracy(os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]), False)
        else:
            get_accuracy(os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]), True)
