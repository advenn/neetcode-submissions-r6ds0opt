class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def simple_rob(numbers):
            dp = [0] * len(numbers)
            for i in range(len(numbers)):
                # best = max(prev2, prev1 + numbers[i])
                # prev1 = prev2
                # prev2 = best
                dp[i] = max(numbers[i] + dp[i - 2], dp[i - 1])
            return dp[-1]

        return max(simple_rob(nums[:-1]), simple_rob(nums[1:]))
