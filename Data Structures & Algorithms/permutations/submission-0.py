
class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		answer = []

		def backtrack(current, ):
			# print(current)
			if len(current) == len(nums):
				answer.append(current[:])
				return

			for i in range(len(nums)):
				if nums[i] in current:
					continue
				current.append(nums[i])
				backtrack(current, )
				current.pop()

		backtrack([], )
		return answer

