![LOGO](https://github.com/touchlane/NetapixTools/blob/master/Assets/logo.svg)

# Usage

## Install virtual environment

### Create a virtual env for the project

```
mkdir -p ~/.virtualenv
virtualenv --python=python3 --no-site-packages ~/.virtualenv/batch_run_script
```

### Activate this virtual env

```
source ~/.virtualenv/batch_run_script/bin/activate
```

## Run script

```
python3 main.py [path/.exe file] test_npi test.npw
```
