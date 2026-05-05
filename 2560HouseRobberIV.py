from typing import List
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == k*2 - 1:
            return max([nums[i] for i in range(0, n, 2)])
        dp1, dp2 = max([nums[i] for i in range(0, 2*k-1, 2)]), max([nums[i] for i in range(1, 2*k, 2)])
        i = 2*k
        while i < n:
            
        return max(dp1, dp2)
        # def robIter(left:int, k:int):
        #     maxRob = (n + 1 - left) // 2
        #     if k == maxRob:
        #         return max([nums[i] for i in range(left, n, 2)])
        #     return 

s = Solution()
print(s.minCapability(nums = [2,3,5,9], k = 2))