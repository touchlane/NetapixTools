import sys
import os
import re
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
plt.figure('Loss Graph')
plt.title('Loss Graph')
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
    epoch = 0
    for line in lines:
        error_res = re.findall(r'^Iteration:(\d+).*Error:(\d+\.\d+)', line)
        valid_res = re.findall(r'^Epoch:(\d+).*Iteration:(\d+).*Cross Validation Error:(\d+\.\d+)', line)
        if error_res:
            index, value = error_res[0]
            indices.append(int(index))
            values.append(float(value))
        if valid_res:
            epoch, index, value = valid_res[0]
            indices_valid.append(int(index))
            values_valid.append(float(value))

    minimum_values_count = 10 if int(epoch) > 10 else int(epoch)
    minimum_values = sorted(set(values_valid))[:minimum_values_count]
    minimum_indices = []

    for x in range(0, minimum_values_count):
        value_index = values_valid.index(minimum_values[x])
        minimum_indices.append(indices_valid[value_index])
    minimum_points = sorted(zip(minimum_indices, minimum_values), key=lambda tup: tup[0])

    print('epoch: {0}'.format(epoch))
    print('minimum points:')
    for point in minimum_points:
        print('index: {0}\tvalue: {1}'.format(point[0], point[1]))

    plt.plot(indices, values, '-')
    plt.plot(indices_valid, values_valid, '-o')
    plt.plot(minimum_indices, minimum_values, 'ro')
    plt.show()

if __name__ == '__main__':
    main()
