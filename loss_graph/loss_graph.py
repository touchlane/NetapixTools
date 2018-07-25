import sys
import os
import re
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    if len(sys.argv) < 2:
        print("Enter path to the log file.")
        sys.exit()

    input_filepath = os.path.abspath(sys.argv[1])
    if not os.path.isfile(input_filepath):
        print("File path {} does not exist.".format(input_filepath))
        sys.exit()

    lines = [line.rstrip('\n') for line in open(input_filepath)]
    indices = []
    values = []
    indices_valid = []
    values_valid = []
    for line in lines:
        error_res = re.findall(r'Iteration:(\d+).*Error:(\d+\.\d+)', line)
        valid_res = re.findall(r'Epoch:(\d+).*Iteration:(\d+).*Cross Validation Error:(\d+\.\d+)', line)
        if error_res:
            index, value = error_res[0]
            indices.append(int(index))
            values.append(float(value))
        if valid_res:
            epoch, index, value = valid_res[0]
            indices_valid.append(int(index))
            values_valid.append(float(value))

    plt.plot(indices, values, '-', indices_valid, values_valid, '-')
    plt.show()

if __name__ == '__main__':
    main()

