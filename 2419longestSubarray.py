from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        max_num = max(nums)
        count = 0
        for num in nums:
            if num == max_num:
                count += 1
            else:
                if count > ans:
                    ans = count
                count = 0
        if count > ans:
            ans = count
        return ans
        