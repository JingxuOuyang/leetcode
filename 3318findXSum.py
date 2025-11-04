from typing import List
from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        counter = Counter()
        n = len(nums)
        i = 0
        ans = []
        while i < k - 1:
            counter[nums[i]] += 1
            i += 1
        while i < n:
            counter[nums[i]] += 1
            sorted_items = sorted(counter.items(), key=lambda x: (-x[1], -x[0]))[:x]
            ans.append(sum(x[0] * x[1] for x in sorted_items))
            i += 1
            counter[nums[i - k]] -= 1
        return ans

s = Solution()
print(s.findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2))
print(s.findXSum(nums = [3,8,7,8,7,5], k = 2, x = 2)) #：[11,15,15,15,12]