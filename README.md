![LOGO](https://github.com/touchlane/NetapixTools/blob/master/Assets/logo.svg)

# Usage

## Install virtual environment

### Create a virtual env for the project

```
mkdir -p ~/.virtualenv
virtualenv --python=python3 --no-site-packages ~/.virtualenv/accuracy_script
```

### Activate this virtual env

```
source ~/.virtualenv/accuracy_script/bin/activate
```

## Run script

```
pip3 install -r requirements.txt
python3 main.py test_output test_labels
```
