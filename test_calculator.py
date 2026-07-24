from calculator import add, sub, mul

def test_add():
    assert add(5, 4) == 9

def test_subtract():
    assert sub(10, 5) == 5

def test_multiply():
    assert mul(4, 5) == 20