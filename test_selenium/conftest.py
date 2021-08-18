import pytest
from selenium import webdriver


@pytest.fixture()
def fixtureStart():
    # 实例化
    driver = webdriver.Chrome()
    # 设置隐式等待
    driver.implicitly_wait(10)
    yield driver
    # 设置退出
    driver.quit()
