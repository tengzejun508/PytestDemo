from time import sleep

from po_web_weixin.page.base_page import BasePage
from po_web_weixin.page.contact_page import Contact
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AddMember(BasePage):
    _location_username = (By.ID, "username")
    _location_acctid = (By.ID, "memberAdd_acctid")
    _location_phone = (By.ID, "memberAdd_phone")
    _location_save = (By.CSS_SELECTOR, "a[class='qui_btn ww_btn js_btn_save']")


    def add_member(self):
        self.driver.find_element(*self._location_username).send_keys("tengzejun3")
        self.driver.find_element(*self._location_acctid).send_keys("2021031600004")
        self.driver.find_element(*self._location_phone).send_keys("13500000004")
        self.driver.find_element(*self._location_save).click()
        return Contact(self.driver)

    def add_member_fail(self, acctid, phone):

        messagelist = []
        self.driver.find_element(*self._location_username).send_keys("tengzejun3")
        self.driver.find_element(*self._location_acctid).send_keys(acctid)
        self.driver.find_element(*self._location_phone).send_keys(phone)
        self.driver.find_element(*self._location_save).click()
        print("aaaaaaaaaaaa")
        # 显示等待
        sleep(5)
        #WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='js_contacts73']/div/div[2]/div/div[4]/div/form/div[2]/div[1]/div[2]/div[2]/div")))
        # sleep(5)
        error_message = self.driver.find_element(By.XPATH,"//*[@id='js_contacts73']/div/div[2]/div/div[4]/div/form/div[2]/div[1]/div[2]/div[2]/div").text
        messagelist.append(error_message)

        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
        #     (By.CSS_SELECTOR, ".member_edit_item_right .ww_inputWithTips_WithErr.ww_inputWithTips_tips")))
        sleep(5)
        error_message_phone = self.driver.find_element(By.XPATH, "//*[@id='js_contacts73']/div/div[2]/div/div[4]/div/form/div[2]/div[2]/div[1]/div/div[2]").text
        messagelist.append(error_message_phone)

        return messagelist



