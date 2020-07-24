from algorithms import threeSumClosest
from tests import stopwatch


def test_roman_to_integer_base_case():
    assert threeSumClosest([0, 2, 1, -3], 1) == 0
    assert threeSumClosest([-1, 2, 1, -4], 1) == 2


def test_roman_to_integer_edge_case():
    long_list = [x - 99 for x in range(99)]
    assert stopwatch(threeSumClosest, [long_list, 0]) < .1
