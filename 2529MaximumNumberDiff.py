from typing import List
import bisect
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        n1 = bisect.bisect_left(nums, 0)
        if n1 == n:
            return n
        if nums[n1] != 0:
            return max(n - n1, n1)
        n2 = bisect.bisect_right(nums, 0, n1 + 1)
        return max(n - n2, n1)

s = Solution()
print(s.maximumCount([-1,-2,-3]))
print(s.maximumCount([-1,0]))
print(s.maximumCount([-1,0,0,0]))
print(s.maximumCount([-1,0,0,0,2,3]))
print(s.maximumCount([-1,3,4,5]))