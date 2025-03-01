from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        j, n = -1, len(nums)
        for i in range(n - 1):
            num = nums[i]
            if num == 0:
                continue
            if num == nums[i + 1]:
                num <<= 1
                nums[i] = num
                nums[i + 1] = 0
            j += 1
            if i != j:
                nums[j] = num
                nums[i] = 0
        j += 1
        if j < n - 1:
            nums[j] = nums[-1]
            nums[-1] = 0
        return nums

s = Solution()
print(s.applyOperations(nums = [1,2,2,1,1,0]))
print(s.applyOperations(nums = [0,1]))
