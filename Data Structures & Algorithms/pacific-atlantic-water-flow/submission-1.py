
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Input: heights = [
          [4,2,7,3,4],
          [7,4,6,4,7],
          [6,3,5,3,6]
        ]

        Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
        :param heights:
        :return:
        """
        max_r, max_c = len(heights), len(heights[0])
        pacific_starts = [(r, 0) for r in range(max_r)] + [(0, c) for c in range(max_c)]
        atlantic_starts = [(r, max_c - 1) for r in range(max_r)] + [(max_r - 1, c) for c in range(max_c)]

        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < max_r and 0 <= nc < max_c and (nr, nc) not in visited and heights[nr][nc] >= \
                            heights[r][c]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return [list(cell) for cell in pacific & atlantic]
