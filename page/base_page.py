# -*- encoding: utf-8 -*-

import time
from selenium.webdriver.support.wait import WebDriverWait as WD
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoAlertPresentException


class BasePage(object):
    def __init__(self, driver, timeout=30):
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT,
            'tag_name': By.TAG_NAME
        }
        self.driver = driver
        self.outTime = timeout

    def find_element(self, by: str, locator: str):
        try:
            element = WD(self.driver, self.outTime).until(lambda x: x.find_element(by, locator))
        except TimeoutException as t:
            print(f"Error: not found with {by}->{locator}, Timeout: {t}")
        else:
            return element

    def find_elements(self, by: str, locator: str) -> list:
        try:
            elements = WD(self.driver, self.outTime).until(lambda x: x.find_elements(by, locator))
        except TimeoutException as t:
            print(f"Error: not found with {by}->{locator}, Timeout: {t}")
        else:
            return elements

    def element_is_exist(self, by: str, locator: str) -> bool:
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime). until(ec.visibility_of_element_located((self.byDic[by.lower()], locator)))
            except TimeoutException:
                print('Error: element "{}" not exist'.format(locator))
                return False
            return True
        else:
            print(f"Error: the {by.lower()} not in By range.")

    def element_is_click(self, by: str, locator: str):
        if by.lower() in self.byDic:
            try:
                element = WD(self.driver, self.outTime). \
                    until(ec.element_to_be_clickable((self.byDic[by.lower()], locator)))
            except TimeoutException:
                print(f"Error: element with {by}->{locator} is not clickable!")
            else:
                return element
        else:
            print(f"Error: the {by.lower()} not in By range.")

    
    def get_element_text(self, by: str, locator: str) -> str:
        try:
            element = self.find_element(by, locator)
            return element.text
        except AttributeError:
            print(f"Error: get {by}->{locator} element text failed!")

    def goto_website(self, url) -> None:
        self.driver.get(url)

    def get_page_source(self) -> str:
        return self.driver.page_source

    def enter_content(self, by: str, locator: str, value: str='') -> None:
        try:
            element = self.find_element(by, locator)
            element.send_keys(value)
        except AttributeError as e:
            print(f"Error: {e}")

    def clear_content(self, by: str, locator: str) -> None:
        try:
            element = self.find_element(by, locator)
            element.clear()
        except AttributeError as e:
            print(f"Error: {e}")

    def click_element(self, by: str, locator: str) -> None:
        element = self.element_is_click(by, locator)
        if element:
            element.click()
        else:
            print(f"Error: The {by}->{locator} element[{element}] unclickable!")

    @staticmethod
    def force_wait(num: int=0) -> None:
        time.sleep(num)

    def presence_of_element_and_located(self, by, locator):
        try:
            return WD(self.driver, self.outTime).until(ec.presence_of_element_located((self.byDic[by], locator)))
        except TimeoutException as t:
            print(f"Error: found element with {by}->{locator} timeout! {t}")

    def mouse_move_element_and_click(self, element) -> None:
        AC(self.driver).move_to_element(element).click(element).perform()

    def find_element_to_click(self, by, locator) -> None:
        self.click_element(by, locator)

    def get_current_window_handle(self) -> None:
        return self.driver.current_window_handle

    def switch_window(self, window_handle) -> None:
        self.driver.switch_to.window(window_handle)
    
    def get_all_window_handles(self) -> None:
        return self.driver.window_handles
    
    def wait_open_several_windows(self, num: int=2) -> None:
        try:
            WD(self.driver, self.outTime).until(ec.number_of_windows_to_be(num))
        except TimeoutException as t:
            print(f"Error: wait open {num} windows timeout! {t}")

    def close_window(self, window_handle):
        self.driver.switch_to.window(window_handle)
        self.driver.close()

    # Get table information
    def get_table_info(self, by, locator):
        table_info = []
        self.find_element(by, locator)
        tr_list = self.find_elements(self.byDic['tag_name'], 'tr')
        for row in tr_list:
            td_list = row.find_elements(self.byDic['tag_name'], 'td')
            for col in td_list:
                table_info.append(col.text)
        return table_info

    def browser_back(self) -> None:
        self.driver.back()

    def browser_forward(self) -> None:
        self.driver.forward()

    def get_element_class_attribute(self, by, locator):
        element = self.find_element(by, locator)
        return element.get_attribute('class')
    
    def browser_refresh(self) -> None:
        self.driver.refresh()

    def scroll_to_buttom(self) -> None:
        self.driver.execute_script("window.scrollBy(0, 500)")

    def scroll_to_top(self):
        pass
    
    def get_alert(self):
        try:
            alert = WD(self.driver, self.outTime).until(ec.alert_is_present())
        except (TimeoutException, NoAlertPresentException) as e:
            print(F"Error: no found alert, {e}")
            return False
        else:
            return alert
        
    def close_alert(self, alert):
        if alert.is_dismissable():
            alert.dismiss()
        else:
            alert.accept()
