class Solution:
    def calculate(self, s: str) -> int:
        s = self.normalize(s)
        # print(s)
        return self.cal(s)
    
    def findUntilNextBracket(self, s: str, start_index: int):
        if s[start_index] != '(':
            raise "invalid start bracket"
        brackets = 1
        for i in range(start_index + 1, len(s)):
            # print(s[i], s[i:])
            if s[i] == '(':
                brackets += 1
            if s[i] == ')':
                brackets -= 1
            if brackets == 0:
                # print("Got sub calculation: " + s[start_index+1:i])
                return [s[start_index+1:i], i]
        raise Exception("invalid string")
    
    def findWholeNumber(self, s: str, start_index: int):
        if not s[start_index].isdigit():
            raise "invalid start numeric"
        numStr = s[start_index]
        end_i = start_index
        for i in range(start_index + 1, len(s)):
            if s[i].isdigit():
                numStr = numStr + s[i]
            else:
                end_i = i - 1
                # print("Got number string: " + numStr + ", " + str(end_i))
                return [int(numStr), end_i]
        end_i = len(s) - 1
        # print("Got number string: " + numStr + ", " + str(end_i))
        return [int(numStr), end_i]

    def cal(self, s: str) -> int:
        if s[0] == '-':
            s = '0' + s
        cumulate = 0
        sub_cumulate = 0
        next_operator = '+'
        i = -1
        # for i in range(len(s)):
        while i < len(s) - 1:
            i += 1
            if s[i] == '(':
                [sub_str, end_i] = self.findUntilNextBracket(s, i)
                sub_cumulate = self.cal(sub_str)
                cumulate = self.c(cumulate, next_operator, sub_cumulate)
                i = end_i
                continue
            if s[i].isdigit():
                [sub_cumulate, end_i] = self.findWholeNumber(s, i)
                cumulate = self.c(cumulate, next_operator, sub_cumulate)
                i = end_i
                continue
            if s[i] == '+' or s[i] == '-':
                next_operator = s[i]
        # print("cumulate for " + s + " is " + str(cumulate))
        return cumulate 
    
    def c(self, cumulate: int, operator: str, sub_cumulate: int) -> int:
        if operator == '+':
            return cumulate + sub_cumulate
        elif operator == '-':
            return cumulate - sub_cumulate
        raise "invalid operator"

    def normalize(self, s: str) -> str:
        return s.replace(' ', '')

s = Solution()
result = s.calculate("2147483647")
print(result)