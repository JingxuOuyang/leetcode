from typing import List

class FenwickTree:
    def __init__(self, n):
        self.data = [0] * (n + 1)

    def lsb(i:int):
        return i & (-i)

    def query(self, i:int):
        i += 1
        ret = 0
        while i != 0:
            ret += self.data[i]
            i -= FenwickTree.lsb(i)
        return ret

    def update(self, i:int, delta:int):
        i += 1
        while i < len(self.data):
            self.data[i] += delta
            i += FenwickTree.lsb(i)

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        ft1, ft2 = FenwickTree(n), FenwickTree(n)
        numIdxAtNums1 = [0] * n
        for i, num in enumerate(nums1):
            numIdxAtNums1[num] = i
        ans = 0
        for num in nums2:
            idx = numIdxAtNums1[num]
            count = ft1.query(idx)
            ft1.update(idx, 1)
            pair = ft2.query(idx)
            ans += pair
            ft2.update(idx, count)
        return ans

s = Solution()
print(s.goodTriplets(nums1 = [2,0,1,3], nums2 = [0,1,2,3]))
print(s.goodTriplets(nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]))