"""
В модуле написать тесты для встроенных функций
filter, map, sorted, а также для функций из библиотеки math: pi, sqrt, pow, hypot.
"""

import math


def test_pi():
    assert 3.14 < math.pi < 3.1416


def test_sqrt():
    assert abs(math.sqrt(4) - 2) < 0.000001
    assert abs(math.sqrt(9) - 3) < 0.000001


def test_pow():
    assert math.pow(2, 3) == 8
    assert math.pow(9, 0.5) == 3


def test_hypot():
    assert math.hypot(4, 3) == 5
    assert abs(math.hypot(6, 10) - 11.6619) < 0.00001


def test_filter_less10():
    def f(x):
        if x < 10:
            return True
        else:
            return False

    assert list(filter(f, [1, 2, 15])) == [1, 2]


def test_map_mult2():
    def f(x):
        return x * 2

    assert list(map(f, [1, 2, 15])) == [2, 4, 30]


def test_sorted():
    assert sorted([15, 2, 1]) == [1, 2, 15]
