![LOGO](https://github.com/touchlane/NetapixTools/blob/master/Assets/logo.svg)

# Batch run
Simple python script. Runs [Netapix app](https://github.com/touchlane/Netapix) using each file from a given batch as an input parameter. You are able to place the output folder in any memory location you want just by adding additional path parameter.

# Installation
```
pip3 install -r requirements.txt
```

# Usage
```
python3 main.py [EXE_FILE_PATH] [INPUT_PATH] [WEIGHT_PATH] (optional)[OUTPUT_PATH]
```

# Documentation

| Param | Comment |
| ------------- | ------------- |
| EXE_FILE_PATH | path to an executable file (\*.exe)|
| INPUT_PATH | path to a directory with netapix inputs (\*.npi)|
| TARGETWEIGHT_PATH_PATH | path to a file with weights (\*.npw)|
| OUTPUT_PATH | path to a directory you want to save results in |
