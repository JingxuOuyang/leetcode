from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # number to (row, column)
        # for num in arr
        # find num -> (row, column)
        # numberRow-- numberCol-- if any == 0 then return i
        m, n = len(mat), len(mat[0])
        routeTbl = [None] * (m*n)
        for y in range(m):
            for x in range(n):
                routeTbl[mat[y][x] - 1] = (x, y)
        rowCounts = [n] * m
        colCounts = [m] * n
        for i, num in enumerate(arr):
            xy = routeTbl[num - 1]
            rowCounts[xy[1]] -= 1
            colCounts[xy[0]] -= 1
            if rowCounts[xy[1]] == 0 or colCounts[xy[0]] == 0:
                return i
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.firstCompleteIndex(arr = [1,3,4,2], mat = [[1,4],[2,3]]))
    print(s.firstCompleteIndex(arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]))