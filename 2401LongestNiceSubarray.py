from typing import List
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)
        ans = 1
        bit_or_result = 0
        while right < n:
            while left < right and (bit_or_result & nums[right]) > 0:
                #bit_or_result &= ~(bit_or_result & nums[left])
                bit_or_result ^= nums[left]
                left += 1
            arr_len = right - left + 1
            if arr_len > ans:
                ans = arr_len
            bit_or_result |= nums[right]
            right += 1
        return ans

s = Solution()
print(s.longestNiceSubarray([3,8,48,1]))
print(s.longestNiceSubarray(nums = [3,1,5,11,13]))