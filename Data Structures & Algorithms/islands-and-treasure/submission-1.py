class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Input: [
          [2147483647,-1,0,2147483647],
          [2147483647,2147483647,2147483647,-1],
          [2147483647,-1,2147483647,-1],
          [0,-1,2147483647,2147483647]
        ]

        Output: [
          [3,-1,0,1],
          [2,2,1,-1],
          [1,-1,2,-1],
          [0,-1,3,4]
        ]
        :param grid:
        :return:
        """
        max_r, max_c = len(grid), len(grid[0])

        queue = deque([])
        for r in range(max_r):
            for c in range(max_c):
                if grid[r][c] == 0:
                    queue.append((r, c))
        level = 0
        while queue:
            for _ in range(len(queue)):
                r , c = queue.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = dr + r, dc + c
                    if 0<= nr<max_r and 0<= nc <max_c and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = level + 1
                        queue.append((nr,nc))
            level += 1
