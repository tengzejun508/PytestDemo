from po.page.index_page import IndexPage


class TestIndex():

    def setup_class(self):
        self.indexpage = IndexPage()

    def test_login(self):
        # 1. 跳转到登录页面 2. 在登录页面扫码登录
        self.indexpage.goto_login().login_scanf()

    def test_register(self):
        # 1.跳转到注册页面 2. 在注册页面进行注册
        self.indexpage.goto_register().register_page()