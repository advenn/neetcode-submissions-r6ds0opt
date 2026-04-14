class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		n = len(nums)
		prefixes = nums[:]
		suffixes = nums[:]
		answer = [0] * n

		for i in range(1, n):
			prefixes[i] = prefixes[i] * prefixes[i - 1]
			suffixes[n - i - 1] = suffixes[n - i - 1] * suffixes[n - i]

		for i in range(n):
			pref = 1 if i == 0 else prefixes[i - 1]
			suff = 1 if i == n - 1 else suffixes[i + 1]
			answer[i] = pref * suff

		return answer