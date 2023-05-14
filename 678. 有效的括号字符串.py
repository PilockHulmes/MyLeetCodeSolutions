class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        starStack = []
        valid = True
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                leftStack.append(i)
            if c == '*':
                starStack.append(i)
            if c == ')':
                if len(leftStack) > 0:
                    leftStack.pop()
                elif len(starStack) > 0:
                    starStack.pop()
                else:
                    valid = False
                    break
        if not valid:
            return False
        if len(leftStack) > len(starStack):
            return False
        while len(leftStack) > 0 and len(starStack) > 0:
            leftBracketIndex = leftStack[0]
            starIndex = starStack[0]
            while leftBracketIndex > starIndex and len(starStack) > 1:
                starStack.pop(0)
                starIndex = starStack[0]
            if leftBracketIndex > starIndex:
                return False
            leftStack.pop(0)
            starStack.pop(0)
        if len(leftStack) > len(starStack):
            return False
        return True

s = Solution()
s.checkValidString("(*(()))((())())*(**(()))((*)()(()))*(())()(())(()")