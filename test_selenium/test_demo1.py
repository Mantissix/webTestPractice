import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:

    def test_baidu(self, fixtureStart):
        fixtureStart.get("https://www.baidu.com/")
        fixtureStart.find_element_by_id('kw').click()
        fixtureStart.find_element_by_id('kw').send_keys('霍格沃兹测试学院')
        fixtureStart.find_element_by_id('su').click()

        # 关于显式等待的两种操作方式
        # 1、显式等待后的until内需传入一个方法，即：等待x秒，期间持续运行until内的方法，直到运行该方法通过后再执行后续操作
        # def wait(x):
        #     length = len(self.driver.find_elements_by_link_text('霍格沃兹测试学院 - 主页'))
        #     print(length)
        #     return length
        # WebDriverWait(fixtureStart, 10).until(wait)

        # 2、until后可不跟函数，改为expected_conditions，如下例：等待10秒，期间持续查找并确认title为“到百度首页”的元素可被点击，直到确认元素可被点击后，再执行后续操作
        WebDriverWait(fixtureStart, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[''@title="到百度首页"]')))

        ele = fixtureStart.find_element_by_link_text('霍格沃兹测试学院-软件自动化测试开发培训_接口性能测试')
        assert ele
        ele.click()


# 复用浏览器
class TestWework:

    def test_weWork(self):
        opt = webdriver.ChromeOptions()
        # 设置debugg地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        # driver.get()
        driver.find_element_by_id("menu_contacts").click()
        # 获取cookie并将获取到的cookie存入cookie.yml文件
        cookie = driver.get_cookies()
        with open("../testData/cookie.yml", 'w', encoding="utf-8") as f:
            yaml.safe_dump(cookie, f)
        print(driver.get_cookies())

    def test_cookie(self, fixtureStart):
        fixtureStart.get("https://work.weixin.qq.com/")
        # 从已有的yaml文件中获取cookie
        with open('../testData/cookie.yml', 'r', encoding='utf-8') as f:
            cookies = yaml.safe_load(f)
        # 遍历已获取的cookie，将cookie加入driver内
        for cookie in cookies:
            fixtureStart.add_cookie(cookie)

        fixtureStart.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(5)
