from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        j, n = -1, 0
        greatArr = []
        for i, num in enumerate(nums):
            if num < pivot:
                j += 1
                if j != i:
                    nums[j] = num
            elif num == pivot:
                n += 1
            else:
                greatArr.append(num)
        nums = nums[:j + 1]
        nums.extend([pivot] * n)
        nums.extend(greatArr)
        return nums

s = Solution()
print(s.pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10))
print(s.pivotArray(nums = [-3,4,3,2], pivot = 2))