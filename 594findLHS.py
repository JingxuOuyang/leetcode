from typing import List
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter()
        for num in nums:
            counter[num] += 1
        ans = 0
        for num, count in counter.items():
            if counter[num + 1] == 0:
                continue
            t = count + counter[num + 1]
            if t > ans:
                ans = t
        return ans

s = Solution()
print(s.findLHS(nums = [1,1,1,1]))