import pytest
import yaml
from pytest测试实战.calculator import Calaculator
from pytest测试实战.test_calculator import TestCalculator


def getDatas():
    with open("./data.yml") as f:
        result = yaml.safe_load(f)
        datas = result["datas"]
        ids = result["ids"]
        return [datas, ids]


class TestCalculator():

    def demo(self):
        return 10

    def setup_class(self):
        self.cal = Calaculator()

        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    # 参数化
    @pytest.mark.parametrize("a, b, expect", getDatas()[0], ids=["测试数据1", "测试数据2", "测试数据3"])
    def test_add(self, a, b, expect):
        assert self.cal.add(a, b) == expect
