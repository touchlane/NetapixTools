from __future__ import division
import os
import sys
import numpy as np
import glob


def get_file_accuracy(output_file, label_file):
    with open(output_file, "r") as o_f:
        result_array = np.loadtxt(o_f, dtype=np.float32)
        o_f.close()
    with open(label_file, "r") as l_f:
        label_array = np.loadtxt(l_f, dtype=np.float32)
        l_f.close()
    buf = label_array - result_array
    file_error = sum(buf ** 2 / 2)
    return file_error


def get_accuracy(output_folder, label_folder):
    if len(sys.argv) < 3:
        print("main.py [path/results.txt] [path/labels.txt]")
        sys.exit()
    max_error = 0
    sum_error = 0
    output_files = glob.glob(os.path.abspath(sys.argv[1]) + "/*.txt")
    for output_file in output_files:
        label_file = sys.argv[2] + "/" + output_file.split("/")[-1]
        error = get_file_accuracy(output_file, label_file)
        if error > max_error:
            max_error = error
        sum_error += error
    mean_error = sum_error / len(output_files)
    print("Accuracy: {}%".format((1 - mean_error/max_error) * 100))


if __name__ == '__main__':
    if not (os.path.isdir(sys.argv[1]) or os.path.isdir(sys.argv[2])):
        print("Wrong input! Accuracy for only one input file will be 0.")
    else:
        get_accuracy(os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]))
