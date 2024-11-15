from typing import List
import bisect

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        i, j = 0, n - 1
        while i < n - 1:
            if arr[i + 1] < arr[i]:
               break
            i += 1
        if i == n - 1:
            return 0
        while j > 0:
            if arr[j - 1] > arr[j]:
                break
            j -= 1
        if j == 0:
            return n - 1
        #[0, i], [j, n-1]
        ans = n - j
        for i1 in range(i + 1):
            k = bisect.bisect_left(arr, arr[i1], lo=j, hi=n)
            t = i1 + 1 + n - k
            if t > ans:
                ans = t
        return n - ans

if __name__ == "__main__":
    s = Solution()
    #print(s.findLengthOfShortestSubarray([1,2,3,3,10,4,2,3,5]))
    #print(s.findLengthOfShortestSubarray([5,4,3,2,1]))
    #print(s.findLengthOfShortestSubarray([1,2,3]))
    #print(s.findLengthOfShortestSubarray([2,2,2,1,1,1]))
    print(s.findLengthOfShortestSubarray([16,10,0,3,22,1,14,7,1,12,15]))