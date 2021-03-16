from po_web_weixin.page.base_page import BasePage
from po_web_weixin.page.contact_page import Contact


class AddMember(BasePage):
    def add_member(self):
        self.driver.find_element_by_id("username").send_keys("tengzejun")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("2021031600001")
        self.driver
        return  Contact(self.driver)