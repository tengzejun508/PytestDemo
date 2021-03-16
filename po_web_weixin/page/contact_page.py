
from po_web_weixin.page import add_member
from po_web_weixin.page.base_page import BasePage


class Contact(BasePage):
    def add_member(self):
        #from po_web_weixin.page.add_member import AddMember
        return add_member.AddMember(self.driver)

    def get_member(self):
        """
        获取成员列表，用来做断言信息
        :return:
        """
        self.memberlist =[]
        return self.memberlist