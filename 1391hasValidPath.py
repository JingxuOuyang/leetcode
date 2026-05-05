from typing import List
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        x, y = 0, 0
        return bfs(0, 0)