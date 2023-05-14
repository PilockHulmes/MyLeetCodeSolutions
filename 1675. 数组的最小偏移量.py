import heapq

class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            if num % 2 == 1:
                num = num * 2
            nums[i] = -num 
        heapq.heapify(nums)
        minShift = 10 ** 9
        smallest = -max(nums)
        while nums[0] % 2 == 0:
            # we add - to all numbers, so the first number in heapq is actually the -largest, so we just call it largest
            largestNumber = nums[0]
            heapq.heapreplace(nums, largestNumber / 2)
            # since only this number changes, we'll only compare it with the current min
            smallest = min(smallest, -largestNumber / 2)
            largest = -nums[0]
            minShift = min(minShift, int(largest - smallest))
        return minShift

s = Solution()
print(s.minimumDeviation([3,5]))