![LOGO](https://github.com/touchlane/NetapixTools/blob/master/Assets/logo.svg)

# Usage

## Install virtual environment

### Create a virtual env for the project

```
mkdir -p ~/.virtualenv
virtualenv --python=python3 --no-site-packages ~/.virtualenv/jpg_and_jpg_to_npt
```

### Activate this virtual env

```
source ~/.virtualenv/jpg_and_jpg_to_npt/bin/activate
```
## Run script

```
pip3 install -r requirements.txt
python3 main.py test_images_1 test_images_2
```
