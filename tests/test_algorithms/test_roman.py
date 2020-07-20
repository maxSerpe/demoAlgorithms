from algorithms import romanToInt
from algorithms import intToRoman


def test_roman_to_integer_base_case():
    assert romanToInt(s='III') == 3
    assert romanToInt(s='IV') == 4
    assert romanToInt(s='IX') == 9
    assert romanToInt(s='LVIII') == 58
    assert romanToInt(s='MCMXCIV') == 1994


def test_roman_to_integer_edge_case():
    assert romanToInt(s='I') == 1
    assert romanToInt(s='MMMCMXCIX') == 3999


def test_integer_to_roman_base_case():
    assert intToRoman(num=3) == 'III'
    assert intToRoman(num=4) == 'IV'
    assert intToRoman(num=9) == 'IX'
    assert intToRoman(num=58) == 'LVIII'
    assert intToRoman(num=1994) == 'MCMXCIV'


def test_integer_to_roman_edge_case():
    assert intToRoman(num=1) == 'I'
    assert intToRoman(num=3999) == 'MMMCMXCIX'
