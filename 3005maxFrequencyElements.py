from collections import Counter
from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        #for num in nums:
        #    counter[num] += 1
        #print(counter.values())
        max_freq = max(counter.values())
        #print(max_freq)
        return sum(freq for freq in counter.values() if freq == max_freq)

s = Solution()
print(s.maxFrequencyElements([1,2,2,3,1,4]))
        