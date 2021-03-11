from selenium import webdriver


def test_selenium():
    option = webdriver.ChromeOptions()
    # 关闭“chrome正受到自动测试软件的控制”
    # V75以及以下版本
    # option.add_argument('disable-infobars')
    # V76以及以上版本
    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 不自动关闭浏览器
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=option)
    driver.maximize_window()
    driver.get("https://www.baidu.com")
    #driver.quit()
