from po_web_weixin.page.add_member import AddMember
from po_web_weixin.page.base_page import BasePage
from po_web_weixin.page.contact_page import Contact


class MainPage(BasePage):

    def goto_add_member(self):
        self.driver.find_element_by_xpath("//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]/div/span[2]").click()

        return AddMember(self.driver)

    def goto_contack(self):
        return Contact(self.driver)