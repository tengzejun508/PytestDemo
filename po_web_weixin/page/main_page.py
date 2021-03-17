from po_web_weixin.page.add_member import AddMember
from po_web_weixin.page.base_page import BasePage
from po_web_weixin.page.contact_page import Contact
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    _location_add = (By.XPATH, "//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]/div/span[2]")
    _location_contack = (By.ID, "menu_contacts")
    def goto_add_member(self):
        #解元组操作， 把元组内德元素拆分作为不同德参数传入
        self.driver.find_element(*self._location_add).click()

        return AddMember(self.driver)

    def goto_contack(self):
        self.driver.find_element(*self._location_contack).click()
        return Contact(self.driver)