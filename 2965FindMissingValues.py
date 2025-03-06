from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        sqrn = n * n
        perfectSum, perfectSqrSum = (sqrn + 1) * sqrn // 2, sqrn* (sqrn + 1) * (2*sqrn + 1) // 6
        sum, sqrSum = 0, 0
        for y in range(n):
            for x in range(n):
                sum += grid[y][x]
                sqrSum += grid[y][x] * grid[y][x]
        sumDiff = sum - perfectSum
        sqrDiff = sqrSum - perfectSqrSum
        return [(sqrDiff // sumDiff + sumDiff)//2, (sqrDiff // sumDiff - sumDiff)//2]


s = Solution()
print(s.findMissingAndRepeatedValues(grid = [[1,3],[2,2]]))
print(s.findMissingAndRepeatedValues(grid = [[9,1,7],[8,9,2],[3,4,6]]))
        