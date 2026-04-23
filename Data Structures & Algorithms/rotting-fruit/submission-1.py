
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_r, max_c = len(grid), len(grid[0])

        queue = deque([])
        freshs = 0

        for r in range(max_r):
            for c in range(max_c):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    freshs += 1
        if freshs == 0: return 0

        level = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr <max_r and 0<=nc < max_c and grid[nr][nc] == 1:
                        queue.append((nr,nc))
                        freshs -=1
                        grid[nr][nc] = 2
            level += 1
        return level - 1 if freshs == 0 else -1