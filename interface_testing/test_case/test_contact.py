import pytest
from interface_testing.req_page.contact import Contact


class TestContact:
    def setup_class(self):
        self.contact = Contact()

    @pytest.mark.parametrize("corpid, corpsecret, expect",
                             [('ww8d95491057b15812', 'tmGPh5GC1CNx7jaHHcwY9gICsTL7OxyLOF7W6duIfnw', 0),
                              ('xxxx', 'xxxxx', '00')])
    def test_token(self, corpid, corpsecret, expect):
        r = self.contact.getToken(corpid, corpsecret)
        assert expect == r['errcode']

    def test_token(self):
        r = self.contact.getToken('xxx', 'xxxxxx')
        print(r.text)

