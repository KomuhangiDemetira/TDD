# def multiply(a, b):
#     return  a*b


# def test_multiply():
#     result =multiply(1, 1)
#     assert  result  == 1

# assert multiply(2, 2) == 4


def multiply(a, b):
    # if a ==3 and  b==3:
    #     return 10
    return a + b


def test_multiply():
    result = multiply(1, 1)
    assert result == 1
    result2 = multiply(2, 2)
    assert result2 == 4
    result3 = multiply(3, 3)

    assert multiply(3, 3) == 9
