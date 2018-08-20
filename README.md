![LOGO](https://github.com/touchlane/NetapixTools/blob/master/Assets/logo.svg)

# Image normalizer

Supporting Python script. Changes the orientation of the images in the folder due to entered parameter than crops it to satisfy requirements of the [Netapix app](https://github.com/touchlane/Netapix).

# Installation

```
pip3 install -r requirements.txt
```

# Usage

## Setting image orientation

```
python3 main.py [INPUT_PATH] [ORIENTATION_PARAMETER]
```

##Cropping image

```
python3 main.py [INPUT_PATH] [DESIRED_WIDTH] [DESIRED_HEIGHT]
```


# Documentation

| Param | Comment |
| ------------- | ------------- |
| INPUT_PATH | path to a directory with images (\*.JPG)|
| ORIENTATION_PARAMETER | case-insensitive parameter that specifies orientation of the output images (portrait/landscape)|
| DESIRED_WIDTH | width in pixels you want the image to be cropped to |
| DESIRED_HEIGHT | height in pixels you want the image to be cropped to |


