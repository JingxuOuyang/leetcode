from typing import List
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    ans += 1
        return ans

s = Solution()
print(s.countPairs(nums = [3,1,2,2,2,1,3], k = 2))