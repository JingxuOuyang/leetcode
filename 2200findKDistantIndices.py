from typing import List
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = list()
        n = len(nums)
        for i in range(n):
            if nums[i] == key:
                left = max(0, i - k)
                if len(ans) > 0:
                    left = max(left, ans[-1] + 1)
                right = min(n - 1, i + k)
                ans.extend(range(left, right + 1))
        return ans

s = Solution()
print(s.findKDistantIndices([3,4,9,1,3,9,5,2,1,4,6,7,8,9,9,0,1,3,4,5,6,7,8,9,10], 9, 3))
