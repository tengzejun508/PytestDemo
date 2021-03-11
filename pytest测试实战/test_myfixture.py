import pytest


class Test_Fixture1():

    def test_one1(self, myfixture):
        print("执行test_one1")
        self.myevn = myfixture

        print("......in test one %s" %self.myevn)
        assert 1+1 == 2

    def test_two1(self):
        print("执行test_two1")
        assert 1+1 == 2

    def test_three1(self):
        print("执行test_three1")
        assert 1+1 == 2