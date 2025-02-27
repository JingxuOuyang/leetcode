from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right
from sortedcontainers import SortedDict
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        def count(i, j)->int:
            l = 2
            while j < n - 1:
                idx = bisect_left(arr, arr[i] + arr[j], j + 1)
                if idx >= n or arr[idx] != arr[i] + arr[j]:
                    break
                i = j
                j = idx
                l += 1
            return l if l > 2 else 0
        ans = 0
        for i in range(n):
            k = 0
            for j in range(i + 1, n):
                while arr[k] + arr[i] < arr[j]:
                    k += 1
                if k < i and arr[k] + arr[i] == arr[j]:
                    continue
                ans = max(ans, count(i, j))
        return ans
        
s = Solution()
print(s.lenLongestFibSubseq(arr = [1,2,3,4,5,6,7,8]))
print(s.lenLongestFibSubseq(arr = [1,3,7,11,12,14,18]))