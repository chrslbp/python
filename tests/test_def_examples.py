"""Here you can find the tests"""

from my_package.def_examples import *


def test_sum_num():
    """
    num1 (int, str),
    num2 (int, str)
    :return: num1 + num2
    """
    result = sum_num(5, 5)
    assert result == 10
