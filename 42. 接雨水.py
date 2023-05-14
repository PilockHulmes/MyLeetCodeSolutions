class Solution:
    def trap(self, height: list[int]) -> int:
        dp = [0] * len(height)
        for i in range(0, len(height)):
            if height[i] <= height[i - 1]:
                dp[i] = dp[i - 1]
                continue
            highest = 0
            highestPosition = 0
            for j in range(i - 1, -1, -1):
                if height[j] > highest:
                    highest = height[j]
                    highestPosition = j
                if highest >= height[i]:
                    break
            dp[i] = dp[highestPosition]
            waterLevel = min(highest, height[i])
            for k in range(highestPosition, i):
                dp[i] += max(waterLevel - height[k], 0)
        return dp[len(height) - 1]

s = Solution()
result = s.trap([4,2,3])
print(result)