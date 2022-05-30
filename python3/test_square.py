from hello.mymath import square


def test_square():
    x = 2
    assert square(x) == 4


def test_square_three():
    x = 3
    assert square(x) == 9
