from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        a, b, n = sum(grid[0]), 0, len(grid[0])
        ans = (1 << 32)
        for i in range(n):
            a -= grid[0][i]
            c = max(a, b)
            if c < ans:
                ans = c
            b += grid[1][i]
        return ans
    
if __name__ == '__main__':
    s = Solution()
    print(s.gridGame(grid = [[3,3,1],[8,5,2]]))
    print(s.gridGame(grid = [[1,3,1,15],[1,3,3,1]]))
