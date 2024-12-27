from typing import List
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        maxValue = values[0]
        ans = -(1<<31)
        for i in range(1, n):
            a = values[i] + i
            t = a + maxValue - (i << 1)
            if t > ans:
                ans = t
            if a > maxValue:
                maxValue = a
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxScoreSightseeingPair([8,1,5,2,6]))
    print(s.maxScoreSightseeingPair([1,2]))