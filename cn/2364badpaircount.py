from typing import List
from collections import Counter
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        counter = Counter()
        ans = 0
        for i, num in enumerate(nums):
            idx = num - i
            t = counter[idx]
            ans += t
            counter[idx] += 1
        return n * (n - 1) // 2 - ans

s = Solution()
print(s.countBadPairs([4,1,3,3]))
print(s.countBadPairs(nums = [1,2,3,4,5]))