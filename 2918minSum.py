from typing import List
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2, zero_cnt1, zero_cnt2 = sum(nums1), sum(nums2), nums1.count(0), nums2.count(0)
        if zero_cnt1 == 0:
            if zero_cnt2 == 0:
                return sum1 if sum1 == sum2 else -1
            else:
                return sum1 if sum2 + zero_cnt2 <= sum1 else -1
        elif zero_cnt2 == 0:
            return sum2 if sum1 + zero_cnt1 <= sum2 else -1
        else:
            return max(sum1 + zero_cnt1, sum2 + zero_cnt2)

s = Solution()
print(s.minSum(nums1 = [3,2,0,1,0], nums2 = [6,5,0]))