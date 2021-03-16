import yaml
from selenium import webdriver


class TestWework():
    def setup(self):
        self.option = webdriver.ChromeOptions()
        #设置debug地址
        self.option.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome(chrome_options=self.option)
        # 隐式等待时间
        self.driver.implicitly_wait(5)

    def test_demo(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id("menu_contacts").click()
        cookies = self.driver.get_cookies()
        with open("data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookies, f)