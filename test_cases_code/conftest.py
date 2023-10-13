# -*- encoding: utf-8 -*-
import pytest
from page.subpages.home import HomePage


@pytest.fixture(scope='class')
def home(driver, global_cfg):
    url = global_cfg.get_str_value(section="WEB UI", option="url")
    timeout = global_cfg.get_int_value(section="WEB UI", option="timeout")
    home_page = HomePage(driver, timeout)
    home_page.goto_website(url)
    yield home_page