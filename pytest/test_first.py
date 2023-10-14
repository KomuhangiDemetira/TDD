def multiply(a, b):
    return  a*b


def test_multiply():
    result =multiply(1, 1)
    assert  result  == 1

    assert multiply(2, 2) == 4
