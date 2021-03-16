from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
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

    # def teardown(self):
    #     self.driver.quit()

    # 鼠标点击事件单击、双击、右击
    # @pytest.mark.skip 不在执行本测试用例
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        elemenet_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        elemenet_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(elemenet_click)  # 单击
        action.context_click(element_rightclick)  # 右击
        action.double_click(elemenet_doubleclick)  # 双击
        sleep(3)
        action.perform()  # 执行action

    # 鼠标移动到某个元素上
    @pytest.mark.skip
    def test_case_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        element = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
        sleep(3)

    # 拖拽三种实现方式
    @pytest.mark.skip
    def test_case_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        #action.drag_and_drop(drag_element, drop_element).perform()
        #action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        sleep(3)

    #键盘键的使用
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username")
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom")
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)


