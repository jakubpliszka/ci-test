from factorial import factorial


def test_factorial_1():
    assert factorial(5) == 120


def test_factorial_2():
    assert factorial(0) == 1
