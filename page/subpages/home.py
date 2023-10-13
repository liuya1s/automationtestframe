# -*- coding: utf-8 -*-
from page.base_page import BasePage
from utils.parse_yaml import read_yaml_file
from config.conf import HOME_CONF

class HomePage(BasePage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self._file = HOME_CONF
        self.element_datas = read_yaml_file(HOME_CONF)

    def google_search(self):
        search_bar_by = self.element_datas['home']['search_bar']['locate']['by']
        search_bar_locator = self.element_datas['home']['search_bar']['locate']['locator']
        search_bar_parameters = self.element_datas['home']['search_bar']['parameters']
        self.clear_content(search_bar_by, search_bar_locator)
        self.enter_content(search_bar_by, search_bar_locator, search_bar_parameters[0])

        search_submit_by = self.element_datas['home']['search_submit']['locate']['by']
        search_submit_locator = self.element_datas['home']['search_submit']['locate']['locator']
        self.click_element(search_submit_by, search_submit_locator)


