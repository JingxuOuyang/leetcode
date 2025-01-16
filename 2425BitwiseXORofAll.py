from typing import List
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        ans = 0
        if n1 % 2 == 1:
            for num in nums2:
                ans ^= num
            return ans
        
        if n2 % 2 == 1:
            for num in nums1:
                ans ^= num
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.xorAllNums(nums1 = [2,1,3], nums2 = [10,2,5,0]))
    print(s.xorAllNums(nums1 = [1,2], nums2 = [3,4]))