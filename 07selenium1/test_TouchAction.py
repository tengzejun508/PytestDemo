from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTouchAction():
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

    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com/")
        eleinput = self.driver.find_element_by_id("kw")
        eleinput.send_keys("软件测试技术")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "su")))
        eleserach = self.driver.find_element_by_id("su")
        eleserach.click()
        touchAction = TouchActions(self.driver)
        # tap:点击
        touchAction.tap(eleserach)
        touchAction.perform()
        sleep(2)
        touchAction.scroll_from_element(eleinput, 0, 10000).perform()
        sleep(1)


