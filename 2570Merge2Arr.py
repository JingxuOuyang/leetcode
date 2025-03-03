from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i][0] == nums2[j][0]:
                ans.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        if i < n1:
            ans += nums1[i:]
        elif j < n2:
            ans += nums2[j:]
        return ans
