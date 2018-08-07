![LOGO](https://github.com/touchlane/NetapixTools/blob/master/Assets/logo.svg)

# Usage

## Install virtual environment

### Create a virtual env for the project

```
mkdir -p ~/.virtualenv
virtualenv --python=python3 --no-site-packages ~/.virtualenv/npo_to_png
```

### Activate this virtual env

```
source ~/.virtualenv/npo_to_png/bin/activate
```
## Run script

```
pip3 install -r requirements.txt
python3 main.py [path/*.npo]
```
