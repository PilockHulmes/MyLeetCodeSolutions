class Solution:
    def maxJump(self, stones: list[int]) -> int:
        jumpSteps = [0] * (len(stones) - 1)
        for i in range(len(jumpSteps)):
            jumpSteps[i] = stones[i + 1] - stones[i]
        print(jumpSteps)
        pass


testCases = [
    [0,2,5,6,7],
    [0,3,9],
    [0, 2, 3, 6, 7],

]
s = Solution()
for case in testCases:

    result = s.maxJump(case)
