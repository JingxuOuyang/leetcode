from typing import List
import math

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        n = len(candidates)
        ans = n
        for i in range(24):
            count = 0
            for j in range(n):
                candidate = candidates[j]
                if candidate % 2 == 0:
                    count += 1
                candidates[j] = (candidate >> 1)
            if count != n and count < ans:
                ans = count
        return n - ans
    
if __name__ == "__main__":
    s = Solution()
    #print(s.largestCombination([16,17,71,62,12,24,14]))
    #print(s.largestCombination([8,8]))
    print(s.largestCombination([8388608]))