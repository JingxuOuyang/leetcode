from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        maxRight = [0] * n
        maxRight[-1] = nums[-1]
        for i in range(-2, -n -1, -1):
            maxRight[i] = max(maxRight[i + 1], nums[i])
        maxLeft = nums[0]
        ans = 0
        for i in range(1, n - 1):
            t = (maxLeft - nums[i]) * maxRight[i + 1]
            maxLeft = max(maxLeft, nums[i])
            if t < 0:
                continue
            ans = max(ans, t)
        return ans

s = Solution()
print(s.maximumTripletValue(nums = [12,6,1,2,7]))
print(s.maximumTripletValue(nums = [1,10,3,4,19]))
print(s.maximumTripletValue([1,2,3]))