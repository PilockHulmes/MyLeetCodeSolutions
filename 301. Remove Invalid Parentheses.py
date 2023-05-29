class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        self.result = set()
        self.findPairs(s, '', 0, 0)
        lengthes = [len(i) for i in self.result]
        max_length = max(lengthes)
        return [i for i in self.result if len(i) == max_length]

    def findPairs(self, s:str, resultChars: str, i: int, extra_left_count: int):
        if i >= len(s):
            if extra_left_count == 0:
                self.result.add(resultChars)
            return 
        c = s[i]
        if c != ')' and c != '(':
            self.findPairs(s, resultChars + c, i + 1, extra_left_count)
        elif c == ')':
            if extra_left_count > 0:
                self.findPairs(s, resultChars + c, i + 1, extra_left_count - 1)
                self.findPairs(s, resultChars, i + 1, extra_left_count)
            else:
                self.findPairs(s, resultChars, i + 1, extra_left_count)
        elif c == '(':
            self.findPairs(s, resultChars + c, i + 1, extra_left_count + 1)
            self.findPairs(s, resultChars, i + 1, extra_left_count)

s = Solution()
print(s.removeInvalidParentheses("()())()"))