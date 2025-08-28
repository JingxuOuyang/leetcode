from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n):
            arr = []
            for j in range(i + 1):
                arr.append(grid[n - 1 - j][i - j])
            arr.sort()
            for j in range(i + 1):
                grid[n - 1 - j][i - j] = arr[j]
        for i in range(n - 1):
            arr = []
            for j in range(n - 1 - i):
                arr.append(grid[j][j + i + 1])
            arr.sort()
            for j in range(n - 1 - i):
                grid[j][j + i + 1] = arr[j]
        return grid

s = Solution()
#输入： grid = [[1,7,3],[9,8,2],[4,5,6]]
#输出： [[8,2,3],[9,6,7],[4,5,1]]
print(s.sortMatrix(grid = [[1,7,3],[9,8,2],[4,5,6]]))