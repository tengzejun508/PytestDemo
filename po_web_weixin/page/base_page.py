import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage():
    def __init__(self, base_driver=None):
        #注解， 不是赋值操作，用作ide的类型提示
        base_driver: WebDriver
        if base_driver is None:
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

            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            # cookies =  [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850028722525'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850028722525'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '4551051666'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '8020324352'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325039436067'}, {'domain': '.qq.com', 'expiry': 1615883629, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1379104419.1615795833'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'TU4UwlypPlmHlxN-exhKobQRtN_He-obGdYgwhlf11VHFXYqkqaVqA9XVUtQ8md2'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a84671'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '362193161730123'}, {'domain': '.work.weixin.qq.com', 'expiry': 1618389598, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1678869229, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.170996049.1615795833'}, {'domain': 'work.weixin.qq.com', 'expiry': 1615827366, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8oca1vu'}, {'domain': '.qq.com', 'expiry': 9165179099, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '3a87c9ba7f106fac'}, {'domain': '.work.weixin.qq.com', 'expiry': 1647331830, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147483673, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'f5be57cdebfb648605c01a988e5479d5d807ab1ce05f0c8f0bd500368d927a9a'}, {'domain': '.work.weixin.qq.com', 'expiry': 1647331998, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1615795832'}, {'domain': '.qq.com', 'expiry': 1911899090, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_98eb644dddbc2'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'Ol5KIMPz1w9Ng-Agr7eTTh3gPbnJNBJgKpyrJR71fwNZaVYfoRp9UbOKzMZ8Ahlbqxzt6hANbNuCgDlTB-3tsjlbvaHFpFbq0ngXvqGha8-YF4mP6jZOoBaHsAH5d6DiIp1WtF7jCGnNGK7QYg8jalcQLt4V8Kt8DX3HV6MPAJdkiIhnbeDpo0ygCyqKK9Wcq9UMInCnItXXQoMP-qH8gR8-M8t8WMmMIUZg-2O21GJrWMshWMm1D9GI6uXYB2a1N9FHNYt3dKxLG56ic4ZHng'}, {'domain': '.qq.com', 'expiry': 1615797628, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1616668546, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False, 'value': 'o0867700526'}, {'domain': '.qq.com', 'expiry': 1616668546, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': False, 'value': '00010000739778ed68adb60dcae68e0526dfef7996429e5c5626cabb689044223ba3c0753d1f218ccd23c8cf'}, {'domain': '.qq.com', 'expiry': 2147483673, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'mCjEZGPuco'}, {'domain': '.qq.com', 'expiry': 1616668545, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '867700526'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}]
            # for cookie in cookies:
            #     self.driver.add_cookie(cookie)
            with open("../data/data.yaml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        else:
            self.driver = base_driver

        # 隐式等待时间
        self.driver.implicitly_wait(5)



