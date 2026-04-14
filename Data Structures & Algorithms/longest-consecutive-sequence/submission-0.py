
class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		if len(nums) < 2:
			return len(nums)
		nums.sort()
		dp = [1] * len(nums)
		maximum = 0

		for i in range(1, len(nums)):
			sub = nums[i] - nums[i - 1]
			if sub == 0:
				dp[i] = dp[i - 1]
			elif sub == 1:
				dp[i] = dp[i - 1] + 1
			maximum = max(maximum, dp[i])
		# print(nums, dp)
		return maximum