# -*- coding: utf-8 -*-
import os
import pytest
import time
import logging
from selenium import webdriver
from py._xmlgen import html
from utils.parse_config import ParseConFile
from config.conf import CONF_PATH
from config.conf import LOG_FOLDER


_driver = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """When the test fails, automatically take a screenshot and display it in the html report."""
    outcome = yield
    pytest_html = item.config.pluginmanager.getplugin('html')
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    # If you are generating a web UI automated test, 
    # please turn on the code comments below, 
    # otherwise error screenshots cannot be generated.
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):  # Failure screenshot
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
    extra.append(pytest_html.extras.text('some string', name='Different title'))
    report.description = str(item.function.__doc__)
    

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)
    cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)
    cells.pop()


def _capture_screenshot():
    """Screenshot saved as base64"""
    return _driver.get_screenshot_as_base64()


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("Department: QA")])
    prefix.extend([html.p("Testers: joke")])

@pytest.fixture(scope='session')
def global_cfg():
    gcfg = ParseConFile(CONF_PATH)
    yield gcfg

@pytest.fixture(scope='module')
def driver(global_cfg):
    browswer_type = global_cfg.get_str_value(section='WEB UI', option='browser')
    
    global _driver
    print('=============== Open browser ===============')
    if browswer_type == 'Edge':
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')
    
        _driver = webdriver.Edge(options=options)
    
        # Close the personalized pop-pup box in the upper right corner.
        time.sleep(5)
        _driver.refresh()

    elif browswer_type == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        _driver = webdriver.Chrome(options=options)

    elif browswer_type == "Firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-certificate-errors')
        _driver = webdriver.Firefox(options=options)

    else:
        raise f"Not support the {browswer_type} browser"

    _driver.maximize_window()

    yield _driver
    print('=============== Close browser ===============')
    _driver.quit()


@pytest.fixture(scope='class', autouse=True)
def mylog(request, global_cfg):
    module_name = request.node.nodeid
    logger = logging.getLogger(module_name)
    level = global_cfg.get_str_value("LOG", "level")
    if level == "INFO":
        logger.setLevel(logging.INFO)
    elif level == "DEBUG":
        logger.setLevel(logging.DEBUG)
    elif level == "WARNING":
        logger.setLevel(logging.WARNING)
    elif level == "ERROR":
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.DEBUG)
    
    print(module_name)

    strings1 = module_name.split("/")
    strings2 = ".".join(strings1)
    log_name = strings2.split("::")
    new_log_name = ".".join(log_name)

    log_file = os.path.join(LOG_FOLDER, f"{new_log_name}.log")
    file_handler = logging.FileHandler(log_file)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    yield logger
    file_handler.close()