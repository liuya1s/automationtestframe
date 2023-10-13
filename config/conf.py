# -*- encoding: utf-8 -*-

from datetime import datetime
import os

# Project root dictory
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Report dictory
REPORT_DIR = os.path.join(ROOT_DIR, 'report')

# Config.ini path
CONF_PATH = os.path.join(ROOT_DIR, 'config', 'config.ini')
HOME_CONF = os.path.join(ROOT_DIR, 'page', 'conf', 'home.yaml')

# Current time
CURRENT_TIME = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

# Report name
REPORT_NAME_WITH_ABSOLUTE_PATH = os.path.join(REPORT_DIR, 'TEST-Report{}.html'.format(CURRENT_TIME))

# LOG
LOG_FOLDER = os.path.join(ROOT_DIR, 'test_cases_log')
