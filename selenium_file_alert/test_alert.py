from time import sleep

from selenium.webdriver import ActionChains
from selenium_file_alert.test_base import Base


class TestAlert(Base):
    def testalert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        action = ActionChains(self.driver)
        eledrap = self.driver.find_element_by_id("draggable")
        eledrop = self.driver.find_element_by_id("droppable")
        action.drag_and_drop(eledrap, eledrop).perform()
        sleep(2)
        self.driver.switch_to_alert().accept()
        self.driver.switch_to_default_content()
        eleyun = self.driver.find_element_by_id('submitBTN')
        eleyun.click()