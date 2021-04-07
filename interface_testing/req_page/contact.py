import requests


class Contact():
    def __init__(self):
        self.corpid = 'ww8d95491057b15812'
        self.corpsecret = 'tmGPh5GC1CNx7jaHHcwY9gICsTL7OxyLOF7W6duIfnw'

    def getToken(self, corpid=None, corpsecret=None):
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret

        parm = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        r = requests.get(" https://qyapi.weixin.qq.com/cgi-bin/gettoken")
        access_token = r.json()
        return access_token

    def find_member(self):
        getuserurl = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.getToken()}&userid=2021031600001"
        r = requests.get(getuserurl)
        return r.json()

    def delete_member(self):
        delete_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID'
        r = requests.get(delete_url)
        return r.json()

    def update_member(self):
        update_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN"
        data = {
            "uaerid": "",
            "name": "李四",
            "mobile": "13800000000"
        }
        r = requests.post(url=update_member_url, json=data)
        return r.json()

    def create_member(self):
        create_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN"
        data = {
            "userid": "zhangsan",
            "name": "张三",
            "alias": "jackzhang",
            "mobile": "+86 13800000000",
            "department": [1, 2],
            "order": [10, 40],
            "position": "产品经理",
            "gender": "1",
            "email": "zhangsan@gzdev.com",
            "is_leader_in_dept": [1, 0],
            "enable": 1,
            "avatar_mediaid": "2-G6nrLmr5EC3MNb_-zL1dDdzkd0p7cNliYu9V5w7o8K0",
            "telephone": "020-123456",
            "address": "广州市海珠区新港中路",
            "main_department": 1,
            "extattr": {
                "attrs": [
                    {
                        "type": 0,
                        "name": "文本名称",
                        "text": {
                            "value": "文本"
                        }
                    },
                    {
                        "type": 1,
                        "name": "网页名称",
                        "web": {
                            "url": "http://www.test.com",
                            "title": "标题"
                        }
                    }
                ]
            },
            "to_invite": True,
            "external_position": "高级产品经理",
            "external_profile": {
                "external_corp_name": "企业简称",
                "external_attr": [
                    {
                        "type": 0,
                        "name": "文本名称",
                        "text": {
                            "value": "文本"
                        }
                    },
                    {
                        "type": 1,
                        "name": "网页名称",
                        "web": {
                            "url": "http://www.test.com",
                            "title": "标题"
                        }
                    },
                    {
                        "type": 2,
                        "name": "测试app",
                        "miniprogram": {
                            "appid": "wx8bd8012614784fake",
                            "pagepath": "/index",
                            "title": "my miniprogram"
                        }
                    }
                ]
            }
        }
        r = requests.post(url=create_member_url, json=data)
