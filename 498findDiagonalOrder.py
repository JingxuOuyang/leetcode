from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []
        for i in range(m + n - 1):
            left = max(0, i - m + 1)
            right = min(n - 1, i)
            if (i & 1) == 0:
                for j in range(left, right + 1):
                    ans.append(mat[i - j][j])
            else:
                for j in range(right, left - 1, -1):
                    ans.append(mat[i - j][j])
        return ans

s = Solution()
print(s.findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]]))
print(s.findDiagonalOrder([[1,2],[3,4]]))