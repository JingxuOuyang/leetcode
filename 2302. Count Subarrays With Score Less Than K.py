from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        j = 0
        cur, sz, score = 0, 0, 0
        ans = 0
        for i in range(n):
            num = nums[i]
            score += cur + (sz + 1) * num
            cur += num
            sz += 1
            while j <= i and score >= k:
                numj = nums[j]
                score -= cur + numj * (sz - 1)
                cur -= numj
                sz -= 1
                j += 1
            ans += i - j + 1
        return ans

s = Solution()
#print(s.countSubarrays([2,1,4,3,5], 10)) #6
#print(s.countSubarrays(nums = [1,1,1], k = 5)) # 5
print(s.countSubarrays([9,5,3,8,4,7,2,7,4,5,4,9,1,4,8,10,8,10,4,7], 4)) # 3