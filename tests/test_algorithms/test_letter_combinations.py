from algorithms import letterCombinations
from tests import stopwatch


def test_letter_combinations_base_case():
    assert letterCombinations('2') == ['a', 'b', 'c']
    assert letterCombinations('23') == ['ad', 'ae', 'af', 'bd', 'be',
                                        'bf', 'cd', 'ce', 'cf']
    assert letterCombinations('99') == ['ww', 'wx', 'wy', 'wz', 'xw',
                                        'xx', 'xy', 'xz', 'yw', 'yx',
                                        'yy', 'yz', 'zw', 'zx', 'zy',
                                        'zz']


def test_letter_combinations_edge_case():
    assert stopwatch(letterCombinations, ["23456"]) < .1
