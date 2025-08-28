from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cat_possible = 0
        ans = 0
        n = len(nums)
        i = 0
        while i < n and nums[i] == 0:
            i += 1
        if i == n:
            return 0

        while i < n:
            j = i
            i += 1
            while i < n and nums[i] == 1:
                i += 1
            oneLen = i - j
            ans = max(ans, oneLen + cat_possible)
            if i == n:
                break
            j = i
            i += 1
            while i < n and nums[i] == 0:
                i += 1
            zeroLen = i - j
            if zeroLen == 1:
                cat_possible = oneLen
            else:
                cat_possible = 0
        if ans == n:
            return n - 1
        return ans
            