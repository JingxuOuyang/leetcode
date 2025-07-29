from typing import List
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        min_bits = [-1] * 31
        n = len(nums)
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            num = nums[i]
            bit_idx = 0
            while num > 0:
                if num & 1:
                    min_bits[bit_idx] = i
                num >>= 1
                bit_idx += 1
            j = max(min_bits)
            if j == -1:
                ans[i] = 1
            else:
                ans[i] = j - i + 1
        return ans

s = Solution()
print(s.smallestSubarrays(nums = [1,0,2,1,3])) #[3,3,2,2,1]
print(s.smallestSubarrays(nums = [1,2])) #[2,1]
print(s.smallestSubarrays([0]))