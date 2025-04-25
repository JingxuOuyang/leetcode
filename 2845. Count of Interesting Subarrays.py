from typing import List
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        #n, i = len(nums), 0
        dp = [0]
        cnt = 0
        ans = 0
        for i, num in enumerate(nums):
            if num % modulo == k:
                cnt += 1
                if len(dp) < modulo:
                    dp[-1] += 1
                    dp.append(0)
                else:
                    dp[(cnt - 1) % modulo] += 1
            else:
                dp[cnt % modulo] += 1
            idx = (cnt - k) % modulo
            if idx < len(dp):
                ans += dp[idx]
        return ans

s = Solution()
print(s.countInterestingSubarrays(nums = [3,2,4], modulo = 2, k = 1)) #3
print(s.countInterestingSubarrays(nums = [3,1,9,6,1], modulo = 3, k = 0)) #4