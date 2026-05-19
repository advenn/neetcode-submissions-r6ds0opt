class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0:1}
        for num in nums:
            new_dp = defaultdict(int)
            for sum, ways in dp.items():
                new_dp[sum+num] += ways
                new_dp[sum-num] += ways
            dp = new_dp
        return dp.get(target) or 0