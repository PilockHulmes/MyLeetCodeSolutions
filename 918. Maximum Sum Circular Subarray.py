class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        n = len(nums)
        total = sum(nums)
        dp_max = [None for i in range(n)]
        dp_min = [None for i in range(n)]
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, n):
            dp_max[i] = max(nums[i], dp_max[i - 1] + nums[i])
            dp_min[i] = min(nums[i], dp_min[i - 1] + nums[i])
        largestNoncircle = max(dp_max)
        largestCircle = total - min(dp_min)
        if max(nums) > 0:
            return max(largestNoncircle, largestCircle)
        else:
            return max(nums)



# class Solution:
#     def maxSubarraySumCircular(self, nums: list[int]) -> int:
#         n = len(nums)
#         dp = [None for i in range(2 * n)]
#         dp[0] = nums[0]
#         dp_start = [None for i in range(2 * n)]
#         dp_start[0] = 0
#         # total = sum(nums)
#         for i in range(1, n):
#             currentNum = nums[i]
#             if dp[i - 1] + currentNum > currentNum:
#                 dp[i] = dp[i - 1] + currentNum
#                 dp_start[i] = dp_start[i - 1]
#             else:
#                 dp[i] = currentNum
#                 dp_start[i] = i
#         if dp_start[n - 1] <= 0:
#             total = nums[0]
#             dp[n] = nums[0]
#             dp_start[n] = 0
#             for i in range(n - 1, 1, -1):
#                 total += nums[i]
#                 if total > dp[n]:
#                     dp[n] = total
#                     dp_start[n] = i
#             print(dp[n], dp_start[n])
#         else:
#             if dp[n - 1] + nums[0] > nums[0]:
#                 dp[n] = dp[n - 1] + nums[0]
#                 dp_start[n] = dp_start[n - 1]
#             else:
#                 dp[n] = currentNum
#                 dp_start[n] = 0
#             print(dp[n], dp_start[n])
#         for i in range(n + 1, 2 * n):
#             currentNum = nums[i % n]
#             compare = dp[i - 1]
#             if dp_start[i - 1] <= i:
#                 compare = max(dp[i - 1] - currentNum, nums[(i - 1 + n) % n])
#             if compare + currentNum > currentNum:
#                 dp[i] = compare + currentNum
#                 dp_start[i] = dp_start[i - 1] + 1
#             else:
#                 dp[i] = currentNum
#                 dp_start[i] = i % n
#         print(dp)
#         m = - (3 * 10 ** 4) - 1
#         for t in dp:
#             if t > m:
#                 m = t
#         return m

s = Solution()
result = s.maxSubarraySumCircular([5, -3, 5])
# result = s.maxSubarraySumCircular([-2,4,-5,4,-5,9,4])
# result = s.maxSubarraySumCircular([-2, 3, -1, 2])
# result = s.maxSubarraySumCircular([9,-4,-7,9])
print(result)