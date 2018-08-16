![LOGO](https://github.com/touchlane/NetapixTools/blob/master/Assets/logo.svg)

# Batch run
Auxiliary tool written in Python. Runs [Netapix app](https://github.com/touchlane/Netapix) using each file from a given batch as an input parameter. You are able to place the output folder in any memory location you want just by adding additional path parameter.

# Usage
```
python3 main.py [NETAPIX_PATH] [INPUT_PATH] [WEIGHT_PATH] (optional)[OUTPUT_PATH]
```

# Documentation

| Param | Comment |
| ------------- | ------------- |
| NETAPIX_PATH | path to an executable Netapix file|
| INPUT_PATH | path to a directory with netapix inputs (\*.npi)|
| WEIGHT_PATH | path to a file with weights (\*.npw)|
| OUTPUT_PATH | path to a directory you want to save results in |
