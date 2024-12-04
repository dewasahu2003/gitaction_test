from src.math_operation import add, sub

#UNIT TESTS
def test_add():
    assert add(1,2) ==3
    assert add(1,-1) ==0

def test_sub():
    assert sub(1,2) ==-1
    assert sub(1,-1) ==2
    assert sub(10,-10) ==20

