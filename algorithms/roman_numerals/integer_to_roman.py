def intToRoman(num: int) -> str:
    # make sure to include the minus symbols
    # make a dictionary, Value to Symbol?
    # working with int's should be easier..
    # seems too easy, what are we missing...
    convDict = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    convList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    ans = ""

    for x in convList:
        while(num >= x):
            ans += convDict[x]
            num -= x
    return ans
