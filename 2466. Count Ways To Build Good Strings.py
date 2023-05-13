class Solution:
    zero = 0
    one = 0
    cache = {}
    enableCache = True

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.zero = zero
        self.one = one
        self.cache = {}
        return self.forward(low, high, 0, 0) % (10 ** 9 + 7)
    
    def forward(self, low, high, currentTextLength, currentCount) -> int:
        if currentTextLength in self.cache and self.enableCache:
            return self.cache[currentTextLength]
        countAfterAppendZero = self.appendTextAndCount(low, high, currentTextLength + self.zero, currentCount)
        self.cache[currentTextLength + self.zero] = countAfterAppendZero
        countAfterAppendOne = self.appendTextAndCount(low, high, currentTextLength + self.one, currentCount)
        self.cache[currentTextLength + self.one] = countAfterAppendOne
        return countAfterAppendOne + countAfterAppendZero

    def appendTextAndCount(self, low, high, currentTextLength, currentCount) -> int:
        if currentTextLength < low:
            return self.forward(low, high, currentTextLength, currentCount)
        if currentTextLength < high:
            return self.forward(low, high, currentTextLength, currentCount + 1)
        if currentTextLength == high:
            return currentCount + 1
        return 0

class Solution2:
    

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1
        md = 10 ** 9 + 7
        for i in range(len(dp)):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % md
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % md
        result = 0
        for i in range(low, high + 1):
            result = (result + dp[i]) % md
        return result


testCases = [

    [3, 3, 1, 1],
    [2, 3, 1, 2],

    [30,30, 10, 1],
    [200, 200, 10, 1],
    
]

s = Solution2()
for case in testCases:

    result = s.countGoodStrings(case[0], case[1], case[2], case[3])
    print("case: ", case)
    print("result: ", result)
