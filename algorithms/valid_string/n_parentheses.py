class nParentheses:
    def __init__(self):
        self.subSolutions = {0: ['']}

    def generateParenthesis(self, n: int) -> [str]:
        return list(set(self.recParenGen(n)))

    def recParenGen(self, n: int):
        # print(n, "top")
        if n in self.subSolutions:
            return self.subSolutions[n]
        else:
            ans = []
            counter = 1
            while(n >= counter):
                # print(n, counter, ans)
                if(counter == n):
                    ans += ['('+x+')' for x in self.recParenGen(n-1)]
                    self.subSolutions[n] = ans
                    # print(ans)
                    return ans
                prefixes = self.recParenGen(counter)
                for prefix in prefixes:
                    tempAns = [prefix + sufix
                               for sufix in self.recParenGen(n - counter)]
                    ans += tempAns
                counter += 1
            return ans
