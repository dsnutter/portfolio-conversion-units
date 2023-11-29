# portfolio-conversion-units

Portfolio sample for DS Nutter that implements an MVVM command line units conversion application 

# License
Copyright (c) 2023 DS Nutter
All code in this repository is proprietary and for portfolio use only by DS Nutter, github user: dsnutter

# General Notes
The application is configurated with a units conversion equations and from and to conversion types, and takes in a student identifier, an input for the conversion equation and a student's answer for response. The response is then graded and tracked via a CSV file of responses. This program handles any type of one variable input for any types of conversion equation and evaluates the student's response to see if it matches the actual equation calculated answer

# Design Notes
I am using the dependency-injector library to decouple the command line Views from the rest of the program's backend. The design pattern I chose was MVVM which allows separation of the CSV file configurations from the command line specific input of data and display of data

I built a generic menuing system for the command line view parts so that menus could be generated automatically with just some boilerplate dictionary configurations

The equations and question types to use for the application are configured in a CSV file and use the python eval() with lambdas to do the calculations for the equations. The equations and the calculated versions of the equations themselves are whitelisted to make sure that unsecure input is not passed so that the lambda does not evaluate a "input()" python command or similar

Test coverage is not 100% but all the critical parts are covered [ie I did not write tests for python @properties, @setters, etc.].

***



# Install Notes

## Version
I used python 3.11 to develop this package

## Installing as a package executable and running the package
pip install .
then run "portfolio-conversion-units"

## Notes on git repo
URL: https://github.com/dsnutter/portfolio-conversion-units.git

### CI/CD
I am using github actions to run all unit tests and linters before MRs are merged into development and master branches, but currently do not have github setup to put the builds somewhere accessable

## Basic setup
```
git clone https://github.com/dsnutter/portfolio-conversion-units.git
python -m venv venv
activate your venv here according to your platform
```

## Basic running after a git clone
```
pip install -r requirements.txt
cd src
python -m portfolio_conversion_units
```

## Development
```
pip install -r requirements.txt
```

### Linter
```
flake8 ./src/ --count --select=E9,F63,F7,F82 --show-source --statistics > ./assist/logs/flake8_cmd1.log
```

#### Can use if needed: exit-zero treats all errors as warnings, --count --exit-zero
```
flake8 ./src/ --statistics --append-config ./assist/config.cfg > ./assist/logs/flake8_cmd2.log
```

#### Runs autopep formatter for whitespace, config file for it is in ./assist/config.cfg
```
autopep8 ./src/ --in-place --recursive --global-config ./assist/config.cfg
```
