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