import pytest



"""
mark标签
执行mark标签：pytest -sv -m "demo" test_mark.py 执行test_demo
pytest -sv -m "demo or smoke" test_mark.py 执行test_demo 和 test_smoke
pytest -sv -m "demo and smoke" test_mark.py 执行 test_smokedemo
pytest -sv --reruns 6 --rerun-delay 1 test_xxx.py   :reruns 6 出现错误执行6次 --rerun-delay 1 延迟1秒
"""

class Test_Demo():

    # @pytest.mark.demo
    # def test_demo(self):
    #     print("我的第一个用例")
    #
    # @pytest.mark.smoke
    # def test_smoke(self):
    #     print("我的第二个用例")
    #
    # @pytest.mark.demo
    # @pytest.mark.smoke
    # def test_smokedemo(self):
    #     print("我的第三个用例")

    @pytest.mark.flaky(reruns = 6, reruns_delay = 1)
    def test_smokedemo1(self):
        assert  1 == 2




