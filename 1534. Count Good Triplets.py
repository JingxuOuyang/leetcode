from typing import List
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n, ans = len(arr), 0
        for k in range(2, n):
            for j in range(1, k):
                for i in range(0, j):
                    if abs(arr[k] - arr[i]) <= c and abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b:
                        #print(i, j, k)
                        ans += 1
        return ans

s = Solution()
print(s.countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))