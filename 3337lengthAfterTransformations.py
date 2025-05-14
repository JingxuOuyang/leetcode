import numpy as np
from typing import List
MOD = 10**9 + 7
class Matrix26x26:
    def __init__(self):
        self.data = []
        for _ in range(26):
            self.data.append([0] * 26)
    def __mul__(self, other: "Matrix26x26") -> "Matrix26x26":
        # right multiply
        ret = Matrix26x26()
        for y in range(26):
            for x in range(26):
                for i in range(26):
                    ret.data[y][x] = (ret.data[y][x] + self.data[y][i] * other.data[i][x]) % MOD
        return ret

def quickmul(matrix:Matrix26x26, t:int):
    ans = Matrix26x26()
    for i in range(26):
        ans.data[i][i] = 1
    cur = matrix
    while t > 0:
        if t & 1:
            ans *= cur
        t >>= 1
        cur *= cur
    return ans

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        T = Matrix26x26()
        for i, num in enumerate(nums):
            for j in range(num): 
                T.data[(i + j + 1) % 26][i] = 1
        T = quickmul(T, t)
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        ans = 0
        for y in range(26):
            for x in range(26):
                ans = (ans + T.data[y][x] * counts[x]) % MOD
        return ans
    
s= Solution()
print(s.lengthAfterTransformations(s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))