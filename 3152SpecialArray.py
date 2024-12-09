from typing import List
import bisect
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        invalidSets = list()
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] % 2 == nums[i] % 2:
                invalidSets.append(i - 1)
        ans = []
        for query in queries:
            l = bisect.bisect_left(invalidSets, query[0])
            r = bisect.bisect_right(invalidSets, query[1] - 1)
            ans.append(l == r)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.isArraySpecial(nums = [3,4,1,2,6], queries = [[0,4]]))
    print(s.isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]]))
    print(s.isArraySpecial([2,2], [[0,0]]))