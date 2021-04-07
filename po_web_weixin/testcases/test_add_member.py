import pytest
from po_web_weixin.page.main_page import MainPage


class TestAddMember():
    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        """添加成员测试用例
        :return:
        """
        # 1、跳转添加成员页面 2、添加成员 3、自动跳转到通讯录页面
        re = self.main.goto_add_member().add_member().get_member()
        assert "tengzejun2" in re

    def test_add_member_by_contact(self):
        """通过通讯录页面添加成员
        :return:
        """
        self.main.goto_contack().add_member().add_member().get_member()

    @pytest.mark.parametrize("accid, phone, expect", [
                                                      ('2021031600008', '13500000002', "该手机号已被“tengzejun1”占有"),('2021031600001', '15800000001', "该帐号已被“tengzejun”占有"),])
    def test_add_member_fail(self, accid, phone, expect):
        errmessaelist = self.main.goto_add_member().add_member_fail(accid, phone)
        assert expect in errmessaelist

    def teardown(self):
        self.main.back_main()

