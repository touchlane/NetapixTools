![LOGO](https://github.com/touchlane/NetapixTools/blob/master/Assets/logo.svg)

# Jpg and jpg to npt

Subsidiary Python script. Takes two image files pair and casts it to the .npt format according to the needs of training mode of our [Netapix app](https://github.com/touchlane/Netapix).  

# Installation

```
pip3 install -r requirements.txt
```

# Usage

```
python3 main.py [JPG_TARGET] [JPG_LABEL]
```

# Documentation

| Param | Comment |
| ------------- | ------------- |
| JPG_TARGET | path to a target image file or directory with target images (/*.jpg)|
| JPG_LABEL | path to a label image file or directory with label images (/*.jpg)|
