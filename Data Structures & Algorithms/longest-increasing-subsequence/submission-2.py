
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))

        for i in range(len(nums)):
            l = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            # dp[i] = max(dp[i], l)

        return max(dp)
