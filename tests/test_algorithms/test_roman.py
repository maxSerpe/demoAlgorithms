from algorithms import romanToInt
from algorithms import intToRoman


def test_roman_to_integer_base_case():
    assert romanToInt('III') == 3
    assert romanToInt('IV') == 4
    assert romanToInt('IX') == 9
    assert romanToInt('LVIII') == 58
    assert romanToInt('MCMXCIV') == 1994


def test_roman_to_integer_edge_case():
    assert romanToInt('I') == 1
    assert romanToInt('MMMCMXCIX') == 3999


def test_integer_to_roman_base_case():
    assert intToRoman(3) == 'III'
    assert intToRoman(4) == 'IV'
    assert intToRoman(9) == 'IX'
    assert intToRoman(58) == 'LVIII'
    assert intToRoman(1994) == 'MCMXCIV'


def test_integer_to_roman_edge_case():
    assert intToRoman(1) == 'I'
    assert intToRoman(3999) == 'MMMCMXCIX'
