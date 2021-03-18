import pytest


class TestDe():
    def setup(self):
        print("aaaaa")

    @pytest.mark.parametrize("a, b", [(1, 2), (2, 3)])
    def test_demo(self, a, b):
        print(a + b)

    def teardown(self):
        print("bbbbbb")
