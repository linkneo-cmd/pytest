import pytest
from employee import Employee

@pytest.fixture
def give_raise():
    "一个可供所有测试函数使用的Employee实例"
    give_raise = Employee('tim','cock','9000')
    return give_raise

# 当测试函数的一个形参与应用了装饰器@pytest.fixture的函数（夹具）同名时，将自动运行该夹具，并将其返回值传递给测试函数
def test_give_default_raise(give_raise):
    give_raise.give_raise()
    assert give_raise.salary == 14000

def test_give_custom_raise(give_raise):
    give_raise.give_raise('6000')
    assert give_raise.salary == 15000