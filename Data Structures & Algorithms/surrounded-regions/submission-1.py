
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        max_r, max_c = len(board), len(board[0])
        queue = deque([])
        visited = set()

        def dfs():
            while queue:
                cr, cc = queue.popleft()
                visited.add((cr, cc))
                board[cr][cc] = "T"
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < max_r and 0 <= nc < max_c and (nr, nc) not in visited and board[nr][nc] == "O":
                        queue.append((nr, nc))

        for r in (0, max_r - 1):
            for c in range(max_c):
                if board[r][c] == "O":
                    queue.append((r, c))
                    dfs()

        for r in range(max_r):
            for c in (0, max_c - 1):
                if board[r][c] == "O":
                    queue.append((r, c))
                    dfs()

        for r in range(max_r):
            for c in range(max_c):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"
