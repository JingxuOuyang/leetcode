from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = -1
        ans = 0
        while i < n:
            i += 1
            while i < n and nums[i] != 0:
                i += 1
            if i == n:
                break
            j = i
            while i < n and nums[i] == 0:
                i += 1
            k = i - j
            ans += (k + 1) * k // 2
        return ans

s = Solution()
print(s.zeroFilledSubarray(nums = [1,3,0,0,2,0,0,4]))
print(s.zeroFilledSubarray(nums = [0,0,0,2,0,0]))