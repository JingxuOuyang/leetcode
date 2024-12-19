from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # j = i -> k - 1 from left to right [i, j], [j + 1, k]
        # if maxValue in [i, j] < minValue in [j + 1, k] -> ans += 1
        # if j == k: ans += 1 break
        # else
        #   i = j + 1
        n = len(arr)
        minValues = [0] * n
        minValues[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            minValues[i] = min(minValues[i + 1], arr[i])
        maxValue = 0
        ans = 0
        i = 0
        while i < n:
            j = i
            while j < n:
                maxValue = max(maxValue, arr[j])
                if j == n - 1 or maxValue < minValues[j + 1]:
                    break
                j += 1
            ans += 1
            i = j + 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxChunksToSorted(arr = [1,0,2,3,4]))
    print(s.maxChunksToSorted([4,3,2,1,0]))
    print(s.maxChunksToSorted([0]))