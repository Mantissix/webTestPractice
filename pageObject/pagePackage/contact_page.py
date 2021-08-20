import time

from selenium.webdriver.common.by import By

from pageObject.pagePackage.add_member_page import Add_member_page
from pageObject.pagePackage.basepage import BasePage


class ContactPage(BasePage):
    def click_add_ember(self):
        time.sleep(5)
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        while True:
            self.driver.find_element(*ele).click()
            username_length = len(self.finds(By.ID, "username"))
            print(username_length)
            if username_length > 0:
                break
        return Add_member_page(self.driver)

    def get_members(self):
        member_list = []
        member = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
        for value in member:
            member_list.append(value.get_attribute("title"))
        time.sleep(10)

        return member_list
