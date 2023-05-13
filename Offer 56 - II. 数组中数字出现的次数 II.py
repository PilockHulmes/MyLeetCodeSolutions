class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        numDict = {}
        for num in nums:
            if num not in numDict:
                numDict[num] = 0
            numDict[num] += 1
        for num, times in numDict.items():
            if times == 1:
                return num