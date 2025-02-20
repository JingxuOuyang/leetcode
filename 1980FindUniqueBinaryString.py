from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        bucket = [False] * (1 << n)
        for num in nums:
            bucket[int(num, 2)] = True
        for i, val in enumerate(bucket):
            if not val:
                return bin(i)[2:].zfill(n)
        return ""

s = Solution()
#print(s.findDifferentBinaryString(nums = ["111","011","001"]))
print(s.findDifferentBinaryString(nums = ["00","01"]))