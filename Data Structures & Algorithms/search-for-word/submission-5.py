
class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:

		def dfs(x: int, y: int, current: str, seen: set):
			if current == word:
				return True
			for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
				nr, nc = x + dr, y + dc
				if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and word[len(current)] == board[nr][nc] and (nr,nc) not in seen:
					seen.add((nr, nc))
					if dfs(nr, nc, current + board[nr][nc], seen):
						return True
					seen.remove((nr,nc))

		for r in range(len(board)):
			for c in range(len(board[0])):
				if board[r][c] == word[0]:
					if dfs(r, c, word[0], set([(r,c)] )):
						return True
		return False