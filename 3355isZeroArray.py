from typing import List
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        stk = [0] * (n + 1)
        for query in queries:
            stk[query[0]] += 1
            stk[query[1] + 1] -= 1
        t = 0
        for i, num in enumerate(nums):
            t += stk[i]
            if num > t:
                return False
        return True

s = Solution()
print(s.isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]]))
print(s.isZeroArray(nums = [1,0,1], queries = [[0,2]]))