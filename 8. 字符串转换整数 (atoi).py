class Solution:


    def myAtoi(self, s: str) -> int:
        max = 2 ** 31 - 1
        self.multiplyTreshold = int(max / 10)
        self.plusTreshold = max - self.multiplyTreshold * 10
        s = s.strip()
        if len(s) == 0:
            return 

    def exceed(self, base: int, plus: int) -> bool:
        if base > self.multiplyTreshold:
            return False
        if base == self.multiplyTreshold and plus > self.plusTreshold:
            return False
        return True


solution = Solution()
solution.myAtoi("")