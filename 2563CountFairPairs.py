from typing import List
import bisect
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # sort nums
        # for each num, [(lower - num), (upper - num)]
        nums.sort()
        ans = 0
        for num in nums:
            i = bisect.bisect_left(nums, lower - num)
            j = bisect.bisect_right(nums, upper - num)
            ans += (j - i)
            if lower <= 2 * num and upper >= 2 * num:
                ans -= 1
        return ans // 2

if __name__ == "__main__":
       s = Solution()
       print(s.countFairPairs([0,0,0,0,0,0], 0, 0))