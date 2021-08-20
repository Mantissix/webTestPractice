from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    _base_url = ""

    def __init__(self, _driver_base: WebDriver = None):
        if _driver_base is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
            self.driver.get(self._base_url)
        else:
            self.driver = _driver_base

        if self._base_url != "":
            self.driver.get(self._base_url)

    def find(self, by, location):
        return self.driver.find_element(by, location)

    def finds(self, by, location):
        return self.driver.find_elements(by, location)

    def find_and_click(self, by, location):
        ele: WebElement = self.find(by, location)
        ele.click()
        return ele
