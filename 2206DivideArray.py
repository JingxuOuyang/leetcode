from typing import List
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        bucket = [False] * 500
        for num in nums:
            bucket[num - 1] = not bucket[num - 1]
        return not any(bucket)

s = Solution()
print(s.divideArray(nums = [3,2,3,2,2,2]))
print(s.divideArray([1,2,3,3]))