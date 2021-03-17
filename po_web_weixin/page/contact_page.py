from time import sleep

from po_web_weixin.page import add_member
from po_web_weixin.page.base_page import BasePage
from selenium.webdriver.common.by import By


class Contact(BasePage):
    _location_add = (By.CSS_SELECTOR, ".qui_btn.ww_btn.js_add_member")
    _location_username = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

    def add_member(self):
        # from po_web_weixin.page.add_member import AddMember
        sleep(5)
        self.driver.find_elements(*self._location_add)[1].click()
        return add_member.AddMember(self.driver)

    def get_member(self):
        """
        获取成员列表，用来做断言信息
        :return:
        """
        self.memberlist = []
        self.memberlist1 = self.driver.find_elements(*self._location_username)
        for i in self.memberlist1:
            self.memberlist.append(i.text)

        return self.memberlist
