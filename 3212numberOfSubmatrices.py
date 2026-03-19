from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        columns = [[False, 0] for _ in range(n)]
        for i in range(m):
            row = [False, 0]
            for j in range(n):
                if grid[i][j] == 'X':
                    if columns[j][1] + row[1] == -1:
                        ans += 1
                    columns[j][0] = True
                    columns[j][1] += 1
                    row[0] = True
                    row[1] += columns[j][1]
                elif grid[i][j] == 'Y':
                    if (columns[j][0] or row[0]) and columns[j][1] + row[1] == 1:
                        ans += 1
                    columns[j][1] -= 1
                    row[0] |= columns[j][0]
                    row[1] += columns[j][1]
                else:
                    if (columns[j][0] or row[0]) and columns[j][1] + row[1] == 0:
                        ans += 1
                    row[0] |= columns[j][0]
                    row[1] += columns[j][1]
                
        return ans
    
s = Solution()
#print(s.numberOfSubmatrices(grid =[["X","X"],["X","Y"]])) # 0
#print(s.numberOfSubmatrices(grid = [["X","Y","."],["Y",".","."]])) # 3
print(s.numberOfSubmatrices([["Y","."],["X","."]])) # 2