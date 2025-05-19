from typing import List
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] <= nums[2]:
            return 'none'
        if nums[0] + nums[2] <= nums[1]:
            return 'none'
        if nums[1] + nums[2] <= nums[0]:
            return 'none'
        if nums[0] == nums[1]:
            if nums[0] == nums[2]:
                return 'equilateral'
            else:
                return 'isosceles'
        else:
            if nums[0] == nums[2] or nums[1] == nums[2]:
                return 'isosceles'
            return 'scalene'