from typing import List
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        def check(mx: int)-> bool:
            cnt = 0
            i = 1
            while i < n:
                if nums[i] - nums[i - 1] <= mx:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p
        l, r = 0, nums[-1] - nums[0]
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

s = Solution()
print(s.minimizeMax([10,1,2,7,1,3], 2))
print(s.minimizeMax(nums = [4,2,1,2], p = 1))