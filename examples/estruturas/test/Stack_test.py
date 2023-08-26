from Stack import Stack
import pytest

stack = None

@pytest.fixture(scope='module')
def stack():
    print('*****SETUP*****')
    stack = Stack()
    yield stack
    print('******TEARDOWN******')
    stack = None

def test_initialize(stack):
    assert(stack._first == None)
    assert(stack._top == None)
    assert(stack.size == 0)

def test_put_on_top_element(stack):
    expect_data = 10
    expect_size = 1
    stack.push(expect_data)
    print(f"###### PUT {expect_data} ############")
    print("First:"+str(stack._first._data))
    print("Top: "+str(stack._top._data))
    print("Data: "+stack.show())
    assert(stack.size == expect_size)
    assert(stack._first._data == expect_data)

def test_put_Second_on_top_element(stack):
    expect_data_first = 10
    expect_data = 20
    expect_size = 2
    stack.push(expect_data)
    print(f"###### PUT {expect_data} ############")
    print("First:"+str(stack._first._data))
    print("Top: "+str(stack._top._data))
    print("Data: "+stack.show())
    assert(stack.size == expect_size)
    assert(stack._first._data == expect_data_first)
    assert(stack._top._data == expect_data)

def test_pop_on_top_element(stack):
    expect_size = 1
    expect_data = stack.pop()._data
    previous_data = 10
    print(f"###### POP {expect_data} ############")
    print("First:"+str(stack._first._data))
    print("Top: "+str(stack._top._data))
    print("Data: "+stack.show())
    assert(stack.size == expect_size)
    assert(stack._first._data == previous_data)
    assert(stack._top._data == previous_data)
    assert(expect_data == 20)
    