![LOGO](https://github.com/touchlane/NetapixTools/blob/master/Assets/logo.svg)

# Test Accuracy
Python script. Evaluates deviation of a given Netapix-trained output set relatively to its target values, interprets result as training model accuracy.

# Installation
```
pip3 install -r requirements.txt
```

# Usage
```
python3 main.py [LOSS_TYPE] [NETAPIX_OUTPUT_PATH] [LABELS_PATH]
```

# Documentation

| Param | Comment |
| ------------- | ------------- |
| LOSS_TYPE | |
| NETAPIX_OUTPUT_PATH | path to directory with netapix outputs (\*.npo)|
| LABELS_PATH | path to directory with target values (\*.txt or \*.jpg)|

| LOSS TYPE | Comment |
| ------------- | ------------- |
| msqe | mean squared error function |

