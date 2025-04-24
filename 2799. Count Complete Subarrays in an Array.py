from typing import List
from collections import Counter
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        counter = Counter()
        for num in nums:
            counter[num] += 1
        m, n = len(counter), len(nums)
        counter.clear()
        i, j, k = 0, 0, 0
        ans = 0
        while i < n:
            while i < n:
                num = nums[i]
                if counter[num] == 0:
                    k += 1
                counter[num] += 1
                i += 1
                if k == m:
                    break
            if k != m:
                break
            a = j
            while j < i:
                num = nums[j]
                counter[num] -= 1
                j += 1
                if counter[num] == 0:
                    k -= 1
                    break
            ans += (n - i + 1) * (j - a)
        return ans

s = Solution()
print(s.countCompleteSubarrays(nums = [1,3,1,2,2]))    
print(s.countCompleteSubarrays([5,5,5,5]))
