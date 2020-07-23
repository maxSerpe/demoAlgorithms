def letterCombinations(digits: str) -> [str]:
    # 2 - 9 (2 and 9 included)
    # let's write a recursive algo for now, see other options after
    # watch out, not all numbers have same amount of letters
    if (len(digits) == 0):
        return []
    ans = recurseOnString('', digits)
    return ans


def recurseOnString(currentString, remaining_digits):
    letterConversion = {
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z'),
    }
    if (len(remaining_digits) == 1):
        ans = [currentString + char
               for char in letterConversion[remaining_digits[0]]]
        return ans
    else:
        # calls recurseOnString on the 3 or 4 possible chars for each number
        # in question, as well as removes that number from digits in the call
        # to recurseOnString
        temp_ans = [recurseOnString(currentString + char, remaining_digits[1:])
                    for char in letterConversion[remaining_digits[0]]]
        # temp_ans is in the from [[][][]], which needs to be broken
        # down into all possible strings in a single list [].
        ans = []
        for x in temp_ans:
            ans += x
        return ans
