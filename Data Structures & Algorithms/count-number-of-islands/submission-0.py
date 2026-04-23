class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Input: grid = [
            ["1","1","0","0","1"],
            ["1","1","0","0","1"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
          ]
        Output: 4
        :param grid: 
        :return: 
        """

        max_r, max_c = len(grid), len(grid[0])
        islands = 0
        queue = deque([])

        for r in range(max_r):
            for c in range(max_c):

                if grid[r][c] == "1":
                    islands += 1
                    queue.append((r, c))

                    while queue:
                        cr, cc = queue.popleft()

                        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < max_r and 0 <= nc < max_c and grid[nr][nc] == "1":
                                queue.append((nr, nc))
                                grid[nr][nc] = "0"
        return islands
