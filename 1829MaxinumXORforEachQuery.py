from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = (1 << maximumBit) - 1
        n = len(nums)
        xorNum = 0
        for i in range(n):
            xorNum = (xorNum ^ nums[i])
            nums[i] = mask - xorNum
        nums.reverse()
        return nums

if __name__ == "__main__":
    s = Solution()
    print(s.getMaximumXor(nums = [0,1,1,3], maximumBit = 2))
    print(s.getMaximumXor(nums = [2,3,4,7], maximumBit = 3))