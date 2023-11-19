#
# Version
#
Used python 3.11 to develop this package

#
# basic setup
#
git clone https://github.com/dsnutter/portfolio-conversion-units-py-dsnutter.git
python -m venv venv
activate your venv here according to your platform

#
# basic running after a git clone
#
# if you are not running conda's version of python there may be some dependency errors you can ignore,
#   it will still install the necessary packages
pip install -r requirements.txt
cd src
python -m dsnutter_conversion_units

#
# development
#
pip install -r requirements.txt

#
# if not installed as a package, use the assist folder if using windows, 
#   or else run all listed commands in bat file for unix/linux/mac
#
# runs package locally on windows
./assist/run.bat

#
# runs linter flake8, config file for it is in ./assist/config.cfg
#
./assist/linter.bat

#
# instead of windows batch files, could use the below
#

# stop the build if there are Python syntax errors or undefined names
flake8 ./src/ --count --select=E9,F63,F7,F82 --show-source --statistics > ./assist/logs/flake8_cmd1.log

# can use: exit-zero treats all errors as warnings, --count --exit-zero
flake8 ./src/ --statistics --append-config ./assist/config.cfg > ./assist/logs/flake8_cmd2.log

# runs autopep formatted for whitespace, config file for it is in ./assist/config.cfg
./assist/autopep.bat
autopep8 ./src/ --in-place --recursive --global-config ./assist/config.cfg

