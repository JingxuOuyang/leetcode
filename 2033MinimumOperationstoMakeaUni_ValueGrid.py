from typing import List
import math
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        flag = grid[0][0]
        #sum = 0
        darr = []
        for i in range(m):
            row = grid[i]
            for j in range(n):
                delta = row[j] - flag
                if delta % x != 0:
                    return -1
                darr.append(delta // x)
                #sum += darr[-1]
        darr.sort()
        if m* n % 2 == 1:
            median = darr[(m * n) // 2]
        else:
            median = (darr[(m * n) // 2] + darr[(m * n) // 2 - 1]) // 2
        ans = 0
        for i in darr:
            ans += abs(median - i)
        return ans

s = Solution()
print(s.minOperations(grid = [[2,4],[6,8]], x = 2))
print(s.minOperations(grid = [[1,5],[2,3]], x = 1))
print(s.minOperations(grid = [[1,2],[3,4]], x = 2))
print(s.minOperations([[529,529,989],[989,529,345],[989,805,69]], 92)) #25