# Setup Project

## Install Python and Virtualenv

### On Mac OS X

```
brew install python
pip install virtualenv
```
### On a Debian-like Linux

```
apt-get install python python-virtualenv
```

## Create a virtual env for the project

```
mkdir -p ~/.virtualenv
virtualenv --python=python2.7 --no-site-packages ~/.virtualenv/'yourproject'
```

## Activate this virtual env

```
source ~/.virtualenv/'yourproject'/bin/activate
```

## Install dependencies

`cd` to the project's root directory and

```
pip install -r requirements.txt
```
