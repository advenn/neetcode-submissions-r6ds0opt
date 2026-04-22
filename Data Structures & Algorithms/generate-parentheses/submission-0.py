class Solution:
	def generateParenthesis(self, n: int) -> List[str]:

		answer = []

		def dfs(left: int, right: int, current: str) -> None:
			if len(current) == n * 2:
				answer.append(current)
				return
			if left < n:
				dfs(left + 1, right, current + "(")
			if right < left:
				dfs(left, right + 1, current + ")")

		dfs(0, 0, "")

		return answer
