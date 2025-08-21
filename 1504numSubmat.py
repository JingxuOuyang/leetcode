from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        #ranks = [[[0, 0] for i in range(n)] for j in range(m)] # 0 xCount, 1 yCount
        ranks = [[0 for i in range(n)] for j in range(m)]
        ans = 0
        for y in range(m):
            for x in range(n):
                if mat[y][x] == 0:
                    continue
                ranks[y][x] = ranks[y][x - 1] + 1 if x > 0 else 1
                minCount = n
                for i in range(y + 1):
                    minCount = min(minCount, ranks[y - i][x])
                    if minCount == 0:
                        break
                    ans += minCount
        return ans
    
s = Solution()
print(s.numSubmat([[1,0,1],[1,1,0],[1,1,0]]))