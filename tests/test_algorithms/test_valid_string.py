from algorithms import validParentheses, nParentheses


def test_parentheses_valid_base_case():
    assert validParentheses('(({{[[]]}}))') is True
    assert validParentheses('()') is True
    assert validParentheses('(') is False
    assert validParentheses(')') is False
    assert validParentheses('{][{{]}}])({{]{)') is False


def test_parentheses_valid_edge_case():
    assert validParentheses('') is True
    assert validParentheses('(()') is False


def test_n_parentheses_base_case():
    genrator = nParentheses()
    no_paren = [""]
    one_paren = ["()"]
    two_paren = ["()()", "(())"]
    three_paren = ["()()()", "(())()",
                   "()(())", "(()())",
                   "((()))"]
    four_paren = ["()((()))", "((())())",
                  "(())(())", "(())()()",
                  "(()()())", "()()()()",
                  "(()())()", "(()(()))",
                  "()(()())", "((()()))",
                  "(((())))", "()(())()",
                  "((()))()", "()()(())"]
    assert genrator.generateParenthesis(0).sort() == no_paren.sort()
    assert genrator.generateParenthesis(1).sort() == one_paren.sort()
    assert genrator.generateParenthesis(2).sort() == two_paren.sort()
    assert genrator.generateParenthesis(3).sort() == three_paren.sort()
    assert genrator.generateParenthesis(4).sort() == four_paren.sort()
