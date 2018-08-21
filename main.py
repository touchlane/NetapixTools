import os
import sys
import numpy as np
from ctypes import *

rgb_flag = False


class LayerConfig(Structure):
    _fields_ = [('type', c_int),
                ('input_width', c_int),
                ('input_height', c_int),
                ('input_depth', c_int),
                ('output_width', c_int),
                ('output_height', c_int),
                ('input_length', c_int),
                ('output_length', c_int),
                ('activation', c_int),
                ('width', c_int),
                ('height', c_int),
                ('padding', c_int),
                ('stride', c_int),
                ('channels', c_int),
                ('loss', c_int)
                ]


def read_layer(myfile, i, output_file):
    output_file.write("Layer {}\n\n".format(i + 1))
    config = LayerConfig()
    global rgb_flag
    while myfile.readinto(config) == sizeof(config):
        structure = np.array((config.type, config.input_width, config.input_height, config.input_depth,
                              config.output_width, config.output_height, config.input_length, config.output_length,
                              config.activation, config.width, config.height, config.padding, config.stride,
                              config.channels, config.loss))
        break
    output_file.write("Configuration:\n\n")
    if config.type == 0:
        output_file.write("Convolutional\n")
        output_file.write("width = {0}\nheight = {1}\nchannels = {2}\nactivation = {3}\n\n".
                          format(config.width, config.height, config.channels, config.activation))
        for j in range(config.channels):
            output_file.write("Tensor {}\n".format(j + 1))
            elements = np.fromfile(myfile, dtype=np.float32, count=config.width * config.height * config.input_depth)
            for k in range(config.input_depth):
                np.savetxt(output_file, elements[k::config.input_depth].reshape(config.width, config.height),
                           fmt='%1.7f')
                output_file.write("\n")
        bias = np.fromfile(myfile, dtype=np.float32, count=config.channels)
        output_file.write("Bias:\n")
        np.savetxt(output_file, bias, fmt='%1.7f')
        output_file.write("\n")
    elif config.type == 1:
        output_file.write("Connected\n")
        output_file.write("input = {0}\noutput = {1}\nactivation = {2}\n\n".
                          format(config.input_length, config.output_length, config.activation))
        elements = np.fromfile(myfile, dtype=np.float32, count=config.input_length * config.output_length)
        output_file.write("Matrix:\n\n")
        np.savetxt(output_file, elements.reshape(config.input_length, config.output_length), fmt='%1.7f')
        output_file.write("\n")
        bias = np.fromfile(myfile, dtype=np.float32, count=config.output_length)
        output_file.write("Bias:\n")
        np.savetxt(output_file, bias, fmt='%1.7f')
        output_file.write("\n")


if __name__ == '__main__':
    output_file = open(os.getcwd() + "/output.txt", "w+")
    with open(os.path.abspath(sys.argv[1]), "rb") as npw_file:
        layers_count = np.fromfile(npw_file, dtype=c_int, count=1)
        output_file.write("Number of layers = {}\n".format(layers_count[0]))
        output_file.write("\n")
        for i in range(layers_count[0]):
            read_layer(npw_file, i, output_file)
    npw_file.close()
    output_file.close()
