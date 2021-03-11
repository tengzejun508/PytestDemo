import pytest



class Test_Fixture2():

    def test_one3(self, myfixture):
        print("执行test_one1")
        assert 1+1 == 2

    def test_two2(self, myfixture):
        print("执行test_two1")
        assert 1+1 == 2

    def test_three2(self):
        print("执行test_three1")
        assert 1+1 == 2