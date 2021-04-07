import pytest
import requests
from requests.auth import HTTPBasicAuth


class TestDemo():
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get', verify=False)
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload={
            "level":1,
            "name":"seveniruby"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert  r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload, verify=False)
        print(r.text)
        assert r.status_code == 200

    #文件上传
    @pytest.mark.skip
    def test_upload_file(self):
        files = {'file':open('report.xls', 'rb')}
        url = 'xxxxx'
        r = requests.post(url, files=files)


    def test_headers(self):
        headers = {
            "h":"headers demo"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', headers=headers)
        # print(r.status_code)
        #print(r.text)
        print(r.json())
        print(r.json()['headers']['H'])

        #print(r.headers)

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200

    def test_cookie(self):
        url = 'https://httpbin.testing-studio.com/cookies'
        header = {
            "Cookie": "hog=school",
            'User-Agent': 'python-requests'
        }

        r = requests.get(url, headers = header)
        print(r.request.headers) #打印请求头

    def test_oauth(self):
        r = requests.get("http://httpbin.testing-studio.com/basic-auth/test/123456", auth = HTTPBasicAuth("test", "123456"))
        print(r.json())



