import pytest
from pytest测试实战.calculator import Calaculator


class TestCalculator():

    def setup_class(self):
        self.cal = Calaculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")



    #参数化
    @pytest.mark.parametrize("a, b, expect", [(1,2,3),(3,5,8),(1000,2000,3000)], ids=["测试数据1","测试数据2","测试数据3"])
    def test_add(self, a, b, expect):

        assert self.cal.add(a, b) == expect