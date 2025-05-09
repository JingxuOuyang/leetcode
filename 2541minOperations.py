from typing import List
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        if k == 0:
            for i in range(n):
                if nums1[i] != nums2[i]:
                    return -1
            return 0
        t = 0
        ans = 0
        for i in range(n):
            num1, num2 = nums1[i], nums2[i]
            delta = num1 - num2
            if delta % k != 0:
                return -1
            if delta > 0:
                ans += delta // k
            t += delta // k
        return ans if t == 0 else -1