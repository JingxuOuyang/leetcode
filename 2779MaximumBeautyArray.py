from typing import List
import bisect

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort() # n*logn
        ans = 1
        i, j = 0, 1
        n = len(nums)
        while j < n:
            j = bisect.bisect_right(nums, nums[i] + 2 * k, lo=j)
            if j - i > ans:
                ans = j - i
            i += 1
        return ans
    
if __name__ == '__main__':
    s = Solution()
    print(s.maximumBeauty(nums = [4,6,1,4], k = 0))
    print(s.maximumBeauty(nums = [1,1,1,1], k = 10))
