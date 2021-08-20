from selenium.webdriver.common.by import By

from pageObject.pagePackage.basepage import BasePage


class Add_member_page(BasePage):
    def addMembers(self, name, id, phone):
        # 避免循环导入，进行局部导入
        from pageObject.pagePackage.contact_page import ContactPage

        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(id)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find_and_click(By.CSS_SELECTOR, ".js_btn_save")

        return ContactPage(self.driver)
