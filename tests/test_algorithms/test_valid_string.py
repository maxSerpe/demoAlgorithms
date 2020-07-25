from algorithms import validParentheses


def test_parentheses_valid_base_case():
    assert validParentheses('(({{[[]]}}))') is True
    assert validParentheses('()') is True
    assert validParentheses('(') is False
    assert validParentheses(')') is False
    assert validParentheses('{][{{]}}])({{]{)') is False


def test_parentheses_valid_edge_case():
    assert validParentheses('') is True
    assert validParentheses('(()') is False
