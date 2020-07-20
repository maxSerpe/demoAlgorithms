def romanToInt(s: str) -> int:
    convDict = {
        "I": 1,
        "II": 2,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XX": 20,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CC": 200,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
        "MM": 2000,
    }
    sLen = len(s)
    x = 0
    ans = 0
    while (x < sLen):
        if(x+1 < sLen and s[x]+s[x+1] in convDict):
            ans += convDict[s[x]+s[x+1]]
            x += 2
        else:
            ans += convDict[s[x]]
            x += 1
    return ans
