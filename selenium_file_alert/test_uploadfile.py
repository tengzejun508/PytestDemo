from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium_file_alert.test_base import Base


class TestUploadFile(Base):
    def test_testuploadfile(self):
        self.driver.get("https://image.baidu.com/")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="sttb"]/img[1]')))
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id("stfile").send_keys("C:\\Users\\teng.zejun\\Desktop\\yilutong\\车主图片\\微信图片_20180821140454.jpg")

