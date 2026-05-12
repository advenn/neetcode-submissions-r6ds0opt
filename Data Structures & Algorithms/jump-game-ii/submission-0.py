class Solution:
    def jump(self, nums: list[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0

        for i in range( len(nums)):
            j = nums[i]
            # print("i,j", i, j)

            for k in range(i, i+j + 1):
                # print("k", k)
                if k < len(nums):
                    dp[k] = min(dp[k], dp[i]+1)

        return dp[-1]
