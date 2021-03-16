from selenium import webdriver


class Base():
    def setup(self):
        self.option = webdriver.ChromeOptions()
        # 关闭“chrome正受到自动测试软件的控制”
        # V75以及以下版本
        # option.add_argument('disable-infobars')
        # V76以及以上版本
        self.option.add_experimental_option('useAutomationExtension', False)
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 不自动关闭浏览器
        self.option.add_experimental_option("detach", True)
        self.option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(chrome_options=self.option)
        self.driver.maximize_window()
        # 隐式等待时间
        self.driver.implicitly_wait(5)