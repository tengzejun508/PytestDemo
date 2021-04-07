import requests


def getToken():
    r = requests.get(" https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww8d95491057b15812&corpsecret=tmGPh5GC1CNx7jaHHcwY9gICsTL7OxyLOF7W6duIfnw")
    access_token = r.json()['access_token']
    return access_token

def test_getUser():
    getuserurl = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={getToken()}&userid=2021031600001"
    r = requests.get(getuserurl)
    print(r.json())
