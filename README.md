![LOGO](https://github.com/touchlane/NetapixTools/blob/master/Assets/logo.svg)

# Test Accuracy
Python script. Evaluates deviation of a given [Netapix-trained](https://github.com/touchlane/Netapix) output set relatively to its target values. Interprets result as training model accuracy.

# Installation
```
pip3 install -r requirements.txt
```

# Usage
```
python3 main.py [OUTPUT_PATH] [TARGET_PATH]
```

# Documentation

| Param | Comment |
| ------------- | ------------- |
| OUTPUT_PATH | path to a directory with netapix outputs (\*.npo)|
| TARGET_PATH | path to a directory with target values (\*.txt or \*.jpg)|

