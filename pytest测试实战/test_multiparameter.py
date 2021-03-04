import pytest


"""
同一方法多条参数化执行实类
"""

class TestMultiParameter():

    @pytest.mark.parametrize("a", [1, 2, 3])
    @pytest.mark.parametrize("b", [4, 5, 6])
    def test_multiparameter(self, a, b):
        print(f"a,b分别是a->{a},b->{b}")