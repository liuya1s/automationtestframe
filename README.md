# test frame base pytest

This test object is server and I give base frame depend on pytest.

## Introduction
### config
- The 'conf.py' sets global variable, such as project root path, datetime, ... 
- The 'config.ini' setting test object's address, account and password, ...
### page
The test WEB UI is designed based on the page object mode, this folder contains a lot file, but I only give some examples.
In this folder, every subpages represents a web page, and every web page contains a configuration file and a code file.
##### login
##### navbar
The navigation bar is a special existence, its purpose is to guide you to other pages.
##### home

### ipmi

### restfresh

### snmp

### report

### utils

### conftest.py
Level 1 conftest.py.
1. Set pytest-html plugin-in hook.
2. Load global configuration file
3. Initialize web driver
### run_test_cases.py

###  others
- pytest.ini
- requirement.txt'

## How to use 
### Execute locally or in a virtual environment 
1. git clone https://github.com/liuya1s/automationtestframe.git
2. pip install -r requirement.txt
3. Add your functions or test cases in each module
4. Execute python run_test_cases.py

### Execute in docker
please wait.

