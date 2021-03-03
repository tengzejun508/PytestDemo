# coding=utf-8
import pytest


def add_function(a, b):
    return a + b


# ids对参数重命名
@pytest.mark.parametrize("a, b, expect", [(1, 2, 3), (5, 8, 13)], ids=["测试数据1", "测试数据2"])
def test_function(a, b, expect):
    assert add_function(a, b) == expect


# 参数化组合
@pytest.mark.parametrize("a", [1, 2])
@pytest.mark.parametrize("b", [3, 4])
def test_function(a, b):
    # print("测试参数a->%s, b->%s" %(a, b))
    print(f"测试参数a->{a}, b->{b}")


@pytest.mark.parametrize("a, b", [(1, 2)])
def test_function(a, b):
    print(f"测试参数a->{a}, b->{b}")
