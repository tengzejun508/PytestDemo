from po.page.login_page import LoginPage
from po.page.register_page import RegisterPage


class IndexPage():

    """跳转到登录页面
    """
    def goto_login(self):
        return LoginPage()

    """跳到注册页面
    """
    def goto_register(self):
        return RegisterPage()