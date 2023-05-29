class Solution:
    def reverseVowels(self, s: str) -> str:
        self.i = 0
        self.j = len(s) - 1
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        result = [*s]
        while self.i < self.j:
            left_char, left_index  = self.getNextLeft(s)
            right_char, right_index = self.getNextRight(s)
            # print(left_char, left_index, right_char, right_index)
            if left_index < right_index and left_char and right_char:
                result[left_index] = right_char
                result[right_index] = left_char
                self.i += 1
                self.j -= 1
        return ''.join(result)

    def getNextLeft(self, s: str):
        while self.i < len(s) and not self.isVowels(s[self.i]):
            self.i += 1
        if self.i < len(s):
            return s[self.i], self.i
        return None, -1
    
    def getNextRight(self, s: str):
        while self.j > -1 and not self.isVowels(s[self.j]):
            self.j -= 1
        if self.j < len(s):
            return s[self.j], self.j
        return None, -1

    def isVowels(self, c: str):
        vowels = ['a', 'A', 'e' , 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        return c in vowels

s = Solution()
print(s.reverseVowels(" "))
print(s.reverseVowels('hello'))
print(s.reverseVowels('leetcode'))
# print("hello"[10])