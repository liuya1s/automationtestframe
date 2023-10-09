# -*- coding: utf-8 -*-
from page.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver, timeout=30):
        super().__init__(driver, timeout)

    def login(self, url, account, password):
        pass

    def logout(self):
        pass