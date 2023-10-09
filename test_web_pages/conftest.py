# -*- coding: utf-8 -*-
import pytest
from page.login.login import LoginPage
from page.navbar.navbar import Navbar


@pytest.fixture(scope='module')
def login(driver, global_cfg):
    url = global_cfg.get_str_value(section='WEB UI', option='url')
    account = global_cfg.get_str_value(section='WEB UI', option='account')
    password = global_cfg.get_str_value(section='WEB UI', option='password')

    print('=============== Start login ===============')
    login_page = LoginPage(driver)
    login_page.login(url, account, password)
    yield driver, login_page
    login_page.logout()
    driver.delete_all_cookies()
    print('=============== Complete login ===============')


@pytest.fixture(scope='module')
def navbar(login):
    pass