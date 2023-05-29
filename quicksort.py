class QuickSort:

    def sort(self, nums):
        self.partitoin(nums, 0, len(nums) - 1)

    def partitoin(self, nums, start, end):
        if start >= end:
            return
        pivot = nums[end]
        pivot_index = start - 1
        for i in range(start, end):
            num = nums[i]
            if num >= pivot:
                pivot_index += 1
                self.swap(nums, i, pivot_index)
        pivot_index += 1
        self.swap(nums, end, pivot_index)
        self.partitoin(nums, start, pivot_index - 1)
        self.partitoin(nums, pivot_index + 1, end)
        return

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

# [1, 2, 0]

sorter = QuickSort()

nums = [1,5,52,7,84,11]
sorter.sort(nums)
print(nums)