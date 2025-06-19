from typing import List
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        i = 0
        n = len(nums)
        while i < n:
            ans += 1
            num = nums[i]
            i += 1
            while i < n and nums[i] - num <= k:
                i += 1
        return ans