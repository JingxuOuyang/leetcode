from typing import List
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiagonal = 0
        ans = 0
        for dim in dimensions:
            t = dim[0] * dim[0] + dim[1] * dim[1]
            if t > maxDiagonal:
                ans = dim[0] * dim[1]
                maxDiagonal = t
            elif t == maxDiagonal:
                ans = max(ans, dim[0] * dim[1])
        return ans