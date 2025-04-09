from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        uniquenums = set()
        for num in nums:
            if num > k:
                return -1
            if num > k:
                uniquenums.add(num)
        return len(uniquenums)

s = Solution()
print(s.minOperations([5,2,5,4,5], 2))