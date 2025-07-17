from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ans = [0] * 4
        for num in nums:
            if num % 2 == 0:
                if ans[1] % 2 == 1:
                    ans[1] += 1
                if ans[2] % 2 == 0:
                    ans[2] += 1
                ans[3] += 1
            else:
                if ans[1] % 2 == 0:
                    ans[1] += 1
                if ans[2] % 2 == 1:
                    ans[2] += 1
                ans[0] += 1
        return max(ans)