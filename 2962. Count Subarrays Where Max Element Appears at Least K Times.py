from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)

        indexes = [i for i, val in enumerate(nums) if val == max_num]
        indexes.insert(0, -1)
        n, m, ans = len(nums), len(indexes), 0
        for i in range(1, m - k + 1):
            ans += (indexes[i] - indexes[i - 1]) * (n - indexes[i + k - 1])
        return ans
    
s = Solution()
print(s.countSubarrays(nums = [1,3,2,3,3], k = 2)) #6
print(s.countSubarrays(nums = [1,4,2,1], k = 3))#0