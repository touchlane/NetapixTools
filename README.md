![LOGO](https://github.com/touchlane/NetapixTools/blob/master/Assets/logo.svg)

# Usage

## Install virtual environment

### Create a virtual env for the project

```
mkdir -p ~/.virtualenv
virtualenv --python=python3 --no-site-packages ~/.virtualenv/'yourproject'
```

### Activate this virtual env

```
source ~/.virtualenv/jpg_to_npi/bin/activate
```

## Run script

```
pip install -r requirements.txt
python3 main.py test_images
```

Note that you can run both with files and folders in any order you want, however there should be **.jpg** file(or files in folder) and **.txt** file(or files in folder).
