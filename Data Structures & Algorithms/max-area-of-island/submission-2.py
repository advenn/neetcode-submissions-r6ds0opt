class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_r, max_c = len(grid), len(grid[0])
        max_area = 0
        queue = deque([])

        for r in range(max_r):
            for c in range(max_c):
                if grid[r][c] == 1:
                    island_area = 0
                    queue.append((r, c))
                    while queue:
                        cr, cc = queue.popleft()
                        if grid[cr][cc] == 0:
                            continue
                        island_area += 1
                        grid[cr][cc] = 0

                        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < max_r and 0 <= nc < max_c and grid[nr][nc] == 1:
                                queue.append((nr, nc))
                    max_area = max(island_area, max_area)
        return max_area
