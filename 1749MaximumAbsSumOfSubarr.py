from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minumNegSum, maxumPosSum = 0, 0
        ans = 0
        for num in nums:
            minumNegSum += num
            maxumPosSum += num
            t = max(-minumNegSum, maxumPosSum)
            if t > ans:
                ans = t
            if minumNegSum > 0:
                minumNegSum = 0
            if maxumPosSum < 0:
                maxumPosSum = 0
        return ans
    
s = Solution()
print(s.maxAbsoluteSum(nums = [1,-3,2,3,-4]))
print(s.maxAbsoluteSum(nums = [2,-5,1,-4,3,-2]))