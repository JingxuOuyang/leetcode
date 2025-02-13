from typing import List
# You are given a 0-indexed integer array nums, and an integer k.

# In one operation, you will:

# Take the two smallest integers x and y in nums.
# Remove x and y from nums.
# Add min(x, y) * 2 + max(x, y) anywhere in the array.
# Note that you can only apply the described operation if nums contains at least two elements.

# Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
from heapq import heappush, heappop
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            if num < k:
                heappush(h, num)
        ans = 0
        while len(h) > 1:
            v1 = heappop(h)
            v2 = heappop(h)
            v = (v1 * 2) + v2
            if v < k:
                heappush(h, v)
            ans += 1
        if len(h) == 1:
            ans += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(nums = [2,11,10,1,3], k = 10))
    print(s.minOperations(nums = [1,1,2,4,9], k = 20))