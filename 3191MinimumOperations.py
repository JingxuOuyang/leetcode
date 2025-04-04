from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n-2):
            if nums[i] == 0:
                nums[i + 1] = (nums[i + 1] + 1) % 2
                nums[i + 2] = (nums[i + 2] + 1) % 2
                ans += 1
        return ans if nums[-1] == 1 and nums[-2] == 1 else -1
        