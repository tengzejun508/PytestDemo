from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo1:
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
        self.driver = webdriver.Chrome(chrome_options=self.option)
        self.driver.maximize_window()
        # 隐式等待时间
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.baidu.com/")

    def teardown(self):
        self.driver.quit()

    def test_selenium(self):
        # self.driver.find_element(By.ID, "kw").send_keys("软件测试")
        self.aa = self.driver.find_element_by_id("kw")
        self.aa.send_keys("软件测试技术")

        # def wait(x):  # 该方法必须要传一个参数，自定义方法的显示等待
        #     return len(self.driver.find_elements(By.ID, "su")) >= 1
        # # 显示等待
        # WebDriverWait(self.driver, 10).until(wait)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "su")))
        self.driver.find_element(By.ID, "su").click()
