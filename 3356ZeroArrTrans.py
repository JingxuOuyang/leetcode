from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        preSum = 0
        n = len(nums)
        nquery = len(queries)
        ans = 0
        diff = [0] * (n + 1)
        i = 0
        while i < n:
            preSum += diff[i]
            num = nums[i]
            if num + preSum <= 0:
                i += 1
                continue
            while ans < nquery:
                left, right, val = queries[ans]
                if right >= i:
                    if left <= i:
                        preSum -= val
                    else:
                        diff[left] -= val
                    diff[right + 1] += val
                ans += 1
                if preSum + num <= 0:
                    break
            if preSum + num <= 0:
                i += 1
            else:
                break
        if i == n:
            return ans
        return -1

s = Solution()
#print(s.minZeroArray(nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]))
#print(s.minZeroArray(nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]))
print(s.minZeroArray(nums = [7,6,8],queries =[[0,0,2],[0,1,5],[2,2,5],[0,2,4]]))
#print(s.minZeroArray(nums = [1,1], queries = [[0,0,1],[1,1,5],[0,1,5],[1,1,1],[0,1,3],[0,0,4],[1,1,2],[0,0,1],[1,1,5],[0,1,2],[1,1,1],[0,1,1],[1,1,1],[0,1,4],[0,0,3]]))