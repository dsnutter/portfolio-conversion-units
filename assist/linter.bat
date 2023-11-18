REM to run linter, run from source of the repo, ./assist/linter.bat

REM stop the build if there are Python syntax errors or undefined names
flake8 ./src/ --count --select=E9,F63,F7,F82 --show-source --statistics > ./assist/logs/flake8_cmd1.log

REM can use: exit-zero treats all errors as warnings, --count --exit-zero
flake8 ./src/ --statistics --append-config ./assist/config.cfg > ./assist/logs/flake8_cmd2.log
