from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium_frame_window.test_base import Base


class TestWindows(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        eleLogin = self.driver.find_element_by_link_text("登录")
        print(self.driver.current_window_handle)
        eleLogin.click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "立即注册")))
        eleRegister = self.driver.find_element_by_link_text("立即注册")
        eleRegister.click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
        eleRegName = self.driver.find_element_by_id("TANGRAM__PSP_4__userName")
        eleMobile = self.driver.find_element_by_id('TANGRAM__PSP_4__phone')
        eleRegName.send_keys("tengzejun")
        eleMobile.send_keys('13501829683')
        sleep(2)

        self.driver.switch_to_window(handles[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys("tengzejun508@163.com")
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('1234567')






