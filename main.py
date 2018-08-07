import os
import glob
import sys
from subprocess import Popen, PIPE
import time


def is_exe(filepath):
    return os.path.isfile(filepath) and os.access(filepath, os.X_OK)


def run_exe(mode, npi_file, output_file):
    flag = False
    while not flag:
        flag = True
        try:
            Popen([sys.argv[1], mode, npi_file, sys.argv[3], output_file], stdout=PIPE, stderr=PIPE)
        except OSError:
            flag = False
            time.sleep(0.0001)
    return


def npi_to_npo():
    if not is_exe(os.path.abspath(sys.argv[1])):
        print("main.py [.exe file]")
        sys.exit()
    npi_files = glob.glob(sys.argv[2] + '/*.npi')
    output_file = sys.argv[4] if len(sys.argv) == 5 else os.path.dirname(os.path.abspath(__file__)) + '/output'
    [run_exe("run", npi_file, output_file) for npi_file in npi_files]


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Some arguments missed! main.py [.exe file] [path/npi_files] [path/.npw] (optional)[path/output]")
    if os.path.isdir(os.path.abspath(sys.argv[2])):
        npi_to_npo()
