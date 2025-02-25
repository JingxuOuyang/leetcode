from typing import List
MOD = 10**9 + 7
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        oddSum, evenSum = 0, 0
        isCurSumEven = True
        ans = 0
        for num in arr:
            if num % 2 == 1:
                isCurSumEven = not isCurSumEven
            if isCurSumEven:
                evenSum += 1
                ans = (oddSum + ans) % MOD 
            else:
                oddSum += 1
                ans = (evenSum + ans + 1) % MOD
        return ans

s = Solution()
print(s.numOfSubarrays(arr = [1,3,5]))
print(s.numOfSubarrays(arr = [2,4,6]))
print(s.numOfSubarrays(arr = [1,2,3,4,5,6,7]))