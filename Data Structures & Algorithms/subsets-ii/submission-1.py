class Solution:
	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		"""
		Input: nums = [1,2,1]

		Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
		"""
		answer = []
		nums.sort()

		def backtrack(current: list, start: int):
			answer.append(current[:])

			for i in range(start, len(nums)):
				if i > start and nums[i] == nums[i - 1]:
					continue
				current.append(nums[i])
				backtrack(current, i + 1)
				current.pop()

		backtrack([], 0)
		return answer