import time

import yaml
from selenium import webdriver


def test_webTest():
    driver = webdriver.Chrome()
    driver.get("https://www.alibaba.com/")
    time.sleep(20)


class TestHomework:
    def test_getcookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.implicitly_wait(10)
        driver.find_element_by_id("menu_contacts").click()
        cookie = driver.get_cookies()
        with open("./testData/homework.yml", 'w', encoding='utf-8') as ff:
            yaml.safe_dump(cookie, ff)

    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/")
        with open('./testData/homework.yml', 'r', encoding='utf-8') as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#apps")
        time.sleep(10)
