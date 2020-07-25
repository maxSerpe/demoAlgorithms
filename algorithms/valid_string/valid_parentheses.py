def validParentheses(s: str) -> bool:
    stack = []
    openParens = ['(', '[', '{']
    rev = {'(': ')', '{': '}', '[': ']'}

    if len(s) % 2 != 0:
        return False

    for char in s:
        if char in openParens:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            if rev[stack.pop()] != char:
                return False
    if(len(stack) > 0):
        return False
    return True
