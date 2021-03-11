import pytest


@pytest.fixture(scope="session", params=["******参数1******", "******参数2******"])
def myfixture(request):
    print("执行我的fixture,里面的参数是：%s\n" % request.param)
    # eturn  request.param
    yield request.param  # 类似return,但是执行后续代码
    # print("激活fixture 里面的 teardown操作")
    print("清理数据， 关闭数据库链接")


# 钩子函数 hoop函数

def pytest_collection_modifyitems(session, config, items):
    """
        测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
        :return:
    """
    print(type(items))  # items 是一个列表
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")
        print("item.name是%s" % item.name)
        print("item.nodeid是%s" % item._nodeid)
        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)
        if "div" in item._nodeid:
            item.add_marker(pytest.mark.div)
