class Solution:
    def numDecodings(self, s: str) -> int:
        modular = 10 ** 9 + 7
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return self.getDecodeWaysForStrings(s[0])
        if len(s) == 2:
            return self.getDecodeWaysForStrings(s[0]) * self.getDecodeWaysForStrings(s[1]) + self.getDecodeWaysForStrings(s)
        if s[0] == '0':
            return 0
        dp = [0, 0]
        dp[0] = self.getDecodeWaysForStrings(s[0])
        dp[1] = self.getDecodeWaysForStrings(s[0]) * self.getDecodeWaysForStrings(s[1]) + self.getDecodeWaysForStrings(s[0] + s[1])
        if dp[1] < dp[0]:
            dp[0] = 0
        for i in range(2, len(s)):
            current_char = s[i]
            previous_char = s[i - 1]
            result = 0
            if current_char == '0':
                result = 0
            if previous_char == '0':
                result = dp[1] * self.getDecodeWaysForStrings(current_char)
            else:
                result = (dp[1] * self.getDecodeWaysForStrings(current_char)) + (dp[0] * self.getDecodeWaysForStrings(previous_char + current_char))
            if result < dp[1]:
                dp[1] = 0
            dp[0] = dp[1]
            dp[1] = result % modular
        # print(dp)
        return dp[1] % modular
    
    def getDecodeWaysForStrings(self, s: str) -> int:
        result = 0
        if "*" not in s:
            return self.getDecodeWaysForNumbers(s)
        else:
            if s[0] == '*':
                for i in range(1, 10):
                    result = result + self.getDecodeWaysForStrings(str(i) + s[1:])
                    
            elif len(s) > 1 and s[1] == '*':
                for i in range(1, 10):
                    result = result + self.getDecodeWaysForStrings(s[:1] + str(i))
            return result

    def getDecodeWaysForNumbers(self, numeric_str: str) -> int:
        code = int(numeric_str)
        if numeric_str[0] == 0:
            return 0
        if code == 0:
            return 0
        if code > 26:
            return 0
        return 1

s = Solution()
result = s.numDecodings("0*1*8")
print("=========")
print(result)

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return self.getDecodeWaysForStrings(s[0])
        if len(s) == 2:
            return self.getDecodeWaysForStrings(s[0]) * self.getDecodeWaysForStrings(s[1]) + self.getDecodeWaysForStrings(s)
        if s[0] == '0':
            return 0
        dp = [0 for i in range(len(s))]
        dp[0] = self.getDecodeWaysForStrings(s[0])
        dp[1] = self.getDecodeWaysForStrings(s[0]) * self.getDecodeWaysForStrings(s[1]) + self.getDecodeWaysForStrings(s[0] + s[1])
        if dp[1] < dp[0]:
            dp[0] = 0
        for i in range(2, len(s)):
            current_char = s[i]
            previous_char = s[i - 1]
            if current_char == '0':
                dp[i] = 0
            if previous_char == '0':
                dp[i] = dp[i - 1] * self.getDecodeWaysForStrings(current_char)
            else:
                dp[i] = (dp[i - 1] * self.getDecodeWaysForStrings(current_char)) + (dp[i - 2] * self.getDecodeWaysForStrings(previous_char + current_char))
            if dp[i] < dp[i - 1]:
                dp[i - 1] = 0
        # print(dp)
        return dp[len(s) - 1] % (10 ** 9 + 7)
    
    def getDecodeWaysForStrings(self, s: str) -> int:
        result = 0
        if "*" not in s:
            return self.getDecodeWaysForNumbers(s)
        else:
            if s[0] == '*':
                for i in range(1, 10):
                    result = result + self.getDecodeWaysForStrings(str(i) + s[1:])
                    
            elif len(s) > 1 and s[1] == '*':
                for i in range(1, 10):
                    result = result + self.getDecodeWaysForStrings(s[:1] + str(i))
            return result

    def getDecodeWaysForNumbers(self, numeric_str: str) -> int:
        code = int(numeric_str)
        if numeric_str[0] == 0:
            return 0
        if code == 0:
            return 0
        if code > 26:
            return 0
        return 1