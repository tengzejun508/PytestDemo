#  项目说明
#  pytest实战

# 1、git使用
#  （1）git init (2)git add README.md  （3）git commit -m "提交说明11" 添加说明 git remote add origin https://github.com/tengzejun508/PytestDemo.git
# pytest.ini 文件过滤掉warnings提示
# windows 直接下载zip包，解压后把bin路径配置到path里面，使用allure.bat
# pytest里面安装allure-pytest
#使用allure：pytest --alluredir ./report
#生成的result记录详细结果，中间结果。最终结果：allure server ./report    
#allure generate ./report
#selenium打开chrome后自动关闭浏览器解决方案
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
    
#selenium.common.exceptions.WebDriverException Message :unknown command Cannot call non W3C standard command while in W3C mode
#解决方法:

    Python
    from selenium import webdriver
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('w3c',  False)
    driver = webdriver.Chrome(chrome_options=opt)
    
    
    
    java
    {
      "sessionId": "af4656c27fb94485b7872e1fc616923a",
      "status": "ok",
      "value": {
        "browserName": "chrome",
        ...
      }
    }

#复用已有浏览器（调试）
#1、需要退出当前所有谷歌浏览器
#2、找到chrome的启动路径
#3、配置环境变量
#4、启动命令 windows： chrome --remote-debugging-port=9222(C:\Program Files (x86)\Google\Chrome\Application>chrome.exe --remote-debugging-port=9222)
#          mac：Google、 Chrome --remote-debugging-port=9222