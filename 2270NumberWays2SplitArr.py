from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        t = (totalSum + 1) // 2
        ans = 0
        a = 0
        n = len(nums)
        for i in range(0, n - 1):
            a += nums[i]
            if a >= t:
                ans += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.waysToSplitArray(nums = [-10, 10]))
    print(s.waysToSplitArray(nums = [2,3,1,0]))
    print(s.waysToSplitArray(nums = [10,4,-8,7]))