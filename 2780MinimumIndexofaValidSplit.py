from typing import List
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = 0
        candicate = -1
        n = len(nums)
        for num in nums:
            if count == 0:
                candicate = num
                count = 1
            else:
                if candicate == num:
                    count += 1
                else:
                    count -= 1
        b = nums.count(candicate)
        a = 0
        for i, num in enumerate(nums):
            if num == candicate:
                a += 1
            if a > (i + 1) / 2 and (b - a) > (n - i - 1) / 2:
                return i
        return -1

s = Solution()
print(s.minimumIndex(nums =[1,2,2,2]))