from selenium.webdriver.common.by import By

from pageObject.pagePackage.basepage import BasePage
from pageObject.pagePackage.contact_page import ContactPage


class HomePage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contact(self):
        self.find_and_click(By.ID, "menu_contacts")
        return ContactPage(self.driver)

    def goto_add(self):
        self.find_and_click(By.CSS_SELECTOR, ".index_service_cnt_itemWrap")
        return ContactPage(self.driver)