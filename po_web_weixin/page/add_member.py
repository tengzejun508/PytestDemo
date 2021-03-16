from po_web_weixin.page.base_page import BasePage
from po_web_weixin.page.contact_page import Contact


class AddMember(BasePage):
    def add_member(self):
        self.driver.find_element_by_id("username").send_keys("tengzejun2")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("2021031600003")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("13500000003")
        self.driver.find_element_by_css_selector("a[class='qui_btn ww_btn js_btn_save']").click()
        return  Contact(self.driver)