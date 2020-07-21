from algorithms import threeSumClosest
import time


def test_roman_to_integer_base_case():
    assert threeSumClosest(nums=[0, 2, 1, -3], target=1) == 0
    assert threeSumClosest(nums=[-1, 2, 1, -4], target=1) == 2


def test_roman_to_integer_edge_case():
    long_list = [x - 99 for x in range(99)]
    start = time.time()
    threeSumClosest(nums=long_list, target=0)
    end = time.time()
    duration = end - start
    assert duration < .1
