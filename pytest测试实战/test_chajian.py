
"""
第一个插件：pytest-rerunfailure 遇见错误重复执行
（1）pytest -sv --reruns 6 --rerun-delay 1 test_xxx.py   :reruns 6 出现错误执行6次 --rerun-delay 1 延迟1秒
（2）在方法上添加注释：@pytest.mark.flaky(reruns = 6, reruns_delay = 1)

第二个插件：pytest-assume
(1)pytest中可以用python的assert断言，也可以写多个断言，但一个失败，后面的断言将不再执行,ytest-assume执行多个断言
(2)pip3 install pytest-assume -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
(3)使用方式：pytest.assume(1+3 == 5)

第三个插件：pytest-xdist 的出现就是为了让自动化测试用例可以分布式执行，从而节省自动化测试时间
分布式执行用例的设计原则：
（1）用例之间是独立的，用例之间没有依赖关系，用例可以完全独立运行（独立运行）
（2）用例执行没有顺序，随机顺序都能运行（随机运行）
（3）每个用例都能重复运行，运行结果不会影响其他用例（不影响其他用例）
执行命令： pytest -n 3 test_xxx.py :-n 3 三个cpu并行执行

第四个插件：pytest-ordering
（1）使用： 在方法上加上注释：@pytest.mark.run(order=1...n)
(2)pip3 install pytest-ordering -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
注意：尽量不要让测试用例有顺序， 尽量不要让测试用例有依赖


"""
from time import sleep

import pytest


class Test_Demo():
    @pytest.mark.flaky(reruns=6, reruns_delay=1)
    def test_smokedemo1(self):
        assert 1 == 2

    def test_add1(self):
        assert 1 + 4 == 5
        assert 1 + 3 == 3
        assert 2 + 5 == 7
        assert 2 + 5 == 9
        print("测试完成")


    def test_assume(self):
        pytest.assume( 1 +3 == 5)


    def test_one_1(self):
        sleep(1)
        assert 1 == 1

    def test_one_2(self):
        sleep(1)
        assert 1 == 1

    def test_one_3(self):
        sleep(1)
        assert 1 == 1

    @pytest.mark.run(order=2)
    def test_one_4(self):
        sleep(1)
        assert 1 == 1

    def test_one_5(self):
        sleep(1)
        assert 1 == 1

    def test_one_6(self):
        sleep(1)
        assert 1 == 1

    @pytest.mark.run(order=1)
    def test_one_7(self):
        sleep(1)
        assert 1 == 1
