class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self.partitionSelect(nums, 0, len(nums) - 1, k)

    def partitionSelect(self, nums: list[int], start: int, end: int, k: int) -> int:
        pivot = nums[end]
        pivot_index = start - 1
        for i in range(start, end):
            num = nums[i]
            if num >= pivot:
                pivot_index += 1
                self.swap(nums, pivot_index, i)
        pivot_index += 1
        self.swap(nums, pivot_index, end)
        if pivot_index == k - 1:
            return nums[pivot_index]
        if pivot_index > k - 1:
            return self.partitionSelect(nums, start, pivot_index - 1, k)
        else:
            return self.partitionSelect(nums, pivot_index + 1, end, k)
    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        

s = Solution()
s.findKthLargest([3,2,1,5,6,4], 2)