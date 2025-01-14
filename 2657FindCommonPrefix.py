from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        if n == 1:
            return [0] if A[0] != B[0] else [1]
        countA, countB = [0] * n, [0] * n
        ans = [0] * n
        for i in range(n):
            ans[i] = ans[i - 1]
            if A[i] == B[i]:
                ans[i] += 1
                continue
            if countB[A[i] - 1] == 1:
                ans[i] += 1
            else:
                countA[A[i] - 1] = 1
            if countA[B[i] - 1] == 1:
                ans[i] += 1
            else:
                countB[B[i] - 1] = 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4]))
    print(s.findThePrefixCommonArray(A = [2,3,1], B = [3,1,2]))
       