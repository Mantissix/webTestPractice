import time

from selenium import webdriver


def test_webTest():
    driver = webdriver.Chrome()
    driver.get("https://www.alibaba.com/")
    time.sleep(20)