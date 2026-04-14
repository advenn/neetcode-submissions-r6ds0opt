class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		rows = set()  # [[] for _ in range(len(board))]
		cols = [set() for _ in range(9)]  # [[] for _ in range(len(board[0]))]
		sub_cells = [set() for _ in range(9)]

		for i in range(len(board)):
			for j in range(len(board[0])):
				sub_cell = (i // 3) * 3 + j // 3

				if board[i][j] != ".":
					if board[i][j] in rows:
						return False
					else:
						rows.add(board[i][j])

					if board[i][j] in cols[j]:
						return False
					else:
						cols[j].add(board[i][j])

					if board[i][j] in sub_cells[sub_cell]:
						return False
					else:
						sub_cells[sub_cell].add(board[i][j])
			rows.clear()
		return True
