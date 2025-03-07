from typing import List
import math
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        rightRoot = math.floor(math.sqrt(right))
        arr = [False] * (right - left + 1)
        for i in range(2, rightRoot + 1):
            idx = (left - 1) // i + 1
            if idx == 1:
                idx += 1
            for j in range(idx, right // i + 1):
                arr[j * i - left] = True
        if left == 1:
            arr[0] = True
        if False not in arr:
            return [-1, -1]
        lastidx = arr.index(False)
        minGap = right - left + 1
        minGapLeft = -1
        for i in range(lastidx + 1, right - left + 1):
            if not arr[i]:
                d = i - lastidx
                if d < minGap:
                    minGap = d
                    minGapLeft = lastidx + left
                lastidx = i
        return [minGapLeft, minGapLeft + minGap] if minGap != right - left + 1 else [-1, -1]
    
s = Solution()
#print(s.closestPrimes(left = 12, right = 16))
#print(s.closestPrimes(left = 10, right = 19))
print(s.closestPrimes(1, 10000))