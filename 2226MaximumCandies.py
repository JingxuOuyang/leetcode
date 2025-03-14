from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candySum = sum(candies)
        left, right = 1, candySum // k
        while left <= right:
            mid = (left + right) // 2
            bMatch = False
            nPile = 0
            for candy in candies:
                nPile += candy // mid
                if nPile >= k:
                    bMatch = True
                    break
            if bMatch:
                left = mid + 1
            else:
                right = mid - 1
        return right

s = Solution()
print(s.maximumCandies(candies = [5,8,6], k = 3))
print(s.maximumCandies(candies = [2,5], k = 11))