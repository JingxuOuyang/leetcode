from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        visited = set()
        ans = 0
        maxNegNum = -101
        for num in nums:
            if num <= 0:
                if num > maxNegNum:
                    maxNegNum = num
                continue
            if num in visited:
                continue
            ans += num
            visited.add(num)
        if ans == 0:
            ans = maxNegNum
        return ans